from openpyxl import load_workbook
from openpyxl.chart import LineChart, AreaChart, Reference, BarChart
from openpyxl.chart.series import SeriesLabel
from Graficas.Estilos_Graficas import GeneraEstilos_Graficas


class GeneraGraficas:
    def __init__(self):
        self.estilos = GeneraEstilos_Graficas()

    def Grafico_linea(
        self,
        ws,
        min_col,
        min_row,
        max_row,
        title=None,
        y_title=None,
        x_title=None,
        width=24,
        height=12,
        tick_skip=5,
    ):
        # Usamos LineChart directamente para asegurar limpieza
        chart = LineChart()

        # Configuración de los datos (Serie Y)
        data = Reference(ws, min_col=min_col, min_row=min_row, max_row=max_row)
        chart.add_data(data, titles_from_data=True)

        # Configuración de categorías (Eje X - Años)
        cats = Reference(ws, min_col=1, min_row=min_row + 1, max_row=max_row)
        chart.set_categories(cats)

        # Título y dimensiones
        chart.title = title or self.estilos.DEFAULT_TITLE
        chart.width = width
        chart.height = height
        
        # --- FIX RADICAL PARA EL DESCUADRE ---
        # 1. Posición absoluta de los ejes
        chart.x_axis.axPos = "b"  # b = bottom (abajo)
        chart.y_axis.axPos = "l"  # l = left (izquierda)
        
        # 2. Cruce de ejes en el origen/mínimo
        chart.x_axis.crosses = "min"
        chart.y_axis.crosses = "min"
        
        # 3. Posición de etiquetas
        chart.x_axis.tickLblPos = "low"
        chart.y_axis.tickLblPos = "low"

        # 4. Evitar que Excel intente rotar o mover el eje (forzar Categoría)
        chart.x_axis.majorTickMark = "out"
        
        # 5. Leyenda abajo para que no estorbe a los ejes
        chart.legend.position = "b"

        # Títulos de ejes
        if y_title:
            chart.y_axis.title = y_title
        if x_title:
            chart.x_axis.title = x_title

        # Evita que las etiquetas del eje X se amontonen
        if tick_skip:
            chart.x_axis.tickLblSkip = tick_skip
        
        # Rotación de etiquetas para que se lean mejor
        chart.x_axis.textRotation = 0

        # Aplicar colores y grosor de línea
        if self.estilos.CHART_COLORS:
            for i, serie in enumerate(chart.series):
                if i < len(self.estilos.CHART_COLORS):
                    # El color debe ser un string HEX sin el '#'
                    color = self.estilos.CHART_COLORS[i].replace("#", "")
                    serie.graphicalProperties.line.solidFill = color
                    # openpyxl usa EMU para el grosor (1 pt = 12700 EMU)
                    # 25000 EMU es aproximadamente 2 ptos
                    serie.graphicalProperties.line.width = 25000 

        return chart

    def Grafico_areas(
        self,
        ws,
        min_col,
        min_row,
        max_row,
        title=None,
        y_title=None,
        x_title=None,
        width=24,
        height=12,
        tick_skip=5,
        style=10,
        grouping="standard"
    ):
        chart = self.estilos.AREA_CHART()

        # Configuración de los datos
        data = Reference(ws, min_col=min_col, min_row=min_row, max_row=max_row)
        chart.add_data(data, titles_from_data=True)

        # Configuración de categorías (Eje X)
        cats = Reference(ws, min_col=1, min_row=min_row + 1, max_row=max_row)
        chart.set_categories(cats)

        chart.title = title or self.estilos.DEFAULT_TITLE
        chart.width = width
        chart.height = height
        chart.style = style
        chart.grouping = grouping

        # --- FIX PARA EL DESCUADRE (Mismo que LineChart) ---
        chart.x_axis.axPos = "b"
        chart.y_axis.axPos = "l"
        chart.x_axis.crosses = "min"
        chart.y_axis.crosses = "min"
        chart.x_axis.tickLblPos = "low"
        chart.y_axis.tickLblPos = "low"
        chart.legend.position = "b"

        # Títulos de ejes
        if y_title:
            chart.y_axis.title = y_title
        if x_title:
            chart.x_axis.title = x_title

        # Evita amontonamiento
        if tick_skip:
            chart.x_axis.tickLblSkip = tick_skip
        
        # Rotación de etiquetas para que se lean mejor (en grados)
        # -45 suele ser la inclinación estándar para fechas
        chart.x_axis.textRotation = -45

        return chart

    def Barras_Rango(
        self,
        ws,
        min_col,
        min_row,
        max_row,
        title=None,
        y_title=None,
        x_title=None,
        width=24,
        height=12,
        tick_skip=5,
        grouping="standard",
    ):
        chart = self.estilos.BAR_CHART()
        chart.grouping = grouping
        chart.width = width
        chart.height = height
        chart.title = title or self.estilos.DEFAULT_TITLE

        # Configuración de los datos
        data = Reference(ws, min_col=min_col, min_row=min_row, max_row=max_row)
        chart.add_data(data, titles_from_data=True)

        # Configuración de categorías (Eje X)
        cats = Reference(ws, min_col=1, min_row=min_row + 1, max_row=max_row)
        chart.set_categories(cats)

        # --- FIX PARA EL DESCUADRE (Consistencia) ---
        chart.x_axis.axPos = "b"
        chart.y_axis.axPos = "l"
        chart.x_axis.crosses = "min"
        chart.y_axis.crosses = "min"
        chart.x_axis.tickLblPos = "low"
        chart.y_axis.tickLblPos = "low"
        chart.legend.position = "b"

        # Títulos de ejes
        if y_title:
            chart.y_axis.title = y_title
        if x_title:
            chart.x_axis.title = x_title

        # Evita amontonamiento
        if tick_skip:
            chart.x_axis.tickLblSkip = tick_skip
        
        # Rotación de etiquetas
        chart.x_axis.textRotation = -45

        return chart

    def barras_divergente(
        self,
        ws,
        min_col,
        min_row,
        max_row,
        title=None,
        y_title=None,
        x_title=None,
        width=24,
        height=12,
        tick_skip=5,
        grouping="standard",
        chart_type="col",
        y_crosses="autoZero",
        cat_col=1 # Por defecto columna 1, se puede cambiar a 2 si hay índice
    ):
        chart = self.estilos.BAR_CHART()
        chart.grouping = grouping
        chart.type = chart_type # col = vertical bars, bar = horizontal bars
        chart.title = title or self.estilos.DEFAULT_TITLE
        chart.width = width
        chart.height = height

        # Configuración de los datos
        data = Reference(ws, min_col=min_col, min_row=min_row, max_row=max_row)
        chart.add_data(data, titles_from_data=True)

        # Configuración de categorías (Eje X)
        cats = Reference(ws, min_col=cat_col, min_row=min_row + 1, max_row=max_row)
        chart.set_categories(cats)

        # --- CONFIGURACIÓN DE EJES ---
        chart.x_axis.axPos = "b"
        chart.y_axis.axPos = "l"
        chart.x_axis.crosses = y_crosses # Divergente suele cruzar en 0
        chart.y_axis.crosses = "min"
        chart.x_axis.tickLblPos = "low"
        chart.y_axis.tickLblPos = "low"
        chart.legend.position = "b"

        # Títulos de ejes
        if y_title:
            chart.y_axis.title = y_title
        if x_title:
            chart.x_axis.title = x_title

        # Evita amontonamiento
        if tick_skip:
            chart.x_axis.tickLblSkip = tick_skip
        
        # Rotación de etiquetas
        chart.x_axis.textRotation = -45

        # Invertir color si es negativo
        if len(chart.series) > 0:
            chart.series[0].invertIfNegative = True
            chart.series[0].graphicalProperties.solidFill = self.estilos.SOLID_FILLOP2

        return chart

    def multiples_lineas(
        self,
        ws,
        min_col,
        max_col,
        min_row,
        max_row,
        style,
        axistitle,
        width,
        height,
        tickLblSkip,
        title=None,
    ):
        chart = self.estilos.LINE_CHART()

        chart.title = title
        chart.style = style
        chart.y_axis.title = axistitle
        chart.width = width
        chart.height = height

        data = Reference(
            ws, min_col=min_col, max_col=max_col, min_row=min_row, max_row=max_row
        )
        chart.add_data(data, titles_from_data=True)

        cats = Reference(ws, min_col=1, min_row=min_row + 1, max_row=max_row)
        chart.set_categories(cats)

        chart.x_axis.tickLblSkip = tickLblSkip

        if self.estilos.CHART_COLORS:
            for i, serie in enumerate(chart.series):
                if i < len(self.estilos.CHART_COLORS):
                    serie.graphicalProperties.line.solidFill = (
                        self.estilos.CHART_COLORS[i]
                    )
                    serie.graphicalProperties.line.width = self.estilos.LINE_WIDTH

        return chart

    def box_plot(
        self,
        ws,
        min_col,
        max_col,
        min_row,
        max_row,
        title=None,
        y_title=None,
        x_title=None,
        width=24,
        height=12,
        tick_skip=1,
        grouping="standard",
        chart_type="col",
        cat_col=1
    ):
        chart = self.estilos.BAR_CHART()
        chart.type = chart_type
        chart.grouping = grouping
        chart.title = title or self.estilos.DEFAULT_TITLE
        chart.width = width
        chart.height = height

        # Referencia a múltiples columnas para las estadísticas
        data = Reference(
            ws, min_col=min_col, max_col=max_col, min_row=min_row, max_row=max_row
        )
        chart.add_data(data, titles_from_data=True)

        cats = Reference(ws, min_col=cat_col, min_row=min_row + 1, max_row=max_row)
        chart.set_categories(cats)

        # --- FIX PARA EL DESCUADRE ---
        chart.x_axis.axPos = "b"
        chart.y_axis.axPos = "l"
        chart.x_axis.crosses = "min"
        chart.y_axis.crosses = "min"
        chart.x_axis.tickLblPos = "low"
        chart.y_axis.tickLblPos = "low"
        chart.legend.position = "b"

        if y_title:
            chart.y_axis.title = y_title
        if x_title:
            chart.x_axis.title = x_title

        if tick_skip:
            chart.x_axis.tickLblSkip = tick_skip
        
        chart.x_axis.textRotation = -45

        if self.estilos.CHART_COLORS:
            for i, serie in enumerate(chart.series):
                if i < len(self.estilos.CHART_COLORS):
                    serie.graphicalProperties.solidFill = self.estilos.CHART_COLORS[i]

        return chart
