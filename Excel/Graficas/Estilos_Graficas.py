from openpyxl.chart import LineChart, AreaChart, BarChart
from openpyxl.styles import Font


class GeneraEstilos_Graficas:
    def __init__(self):
        self.CHART_COLORS = [
            "4472C4",
            "ED7D31",
            "A9D18E",
            "FF0000",
            "7030A0",
            "FFC000",
            "5B9BD5",
            "70AD47",
            "264478",
            "9E480D",
        ]
        
        self.LINEAR_COLORS = ["#AAAAAA", "#FF6B35", "#1F77B4"]
        self.LINEAR_THICKNESS = [8000, 12000, 20000] 

        self.LINE_CHART = LineChart
        self.AREA_CHART = AreaChart
        self.BAR_CHART = BarChart

        self.TITLE_FONT = Font(name="Arial", size=14, bold=True)
        self.AXIS_FONT = Font(name="Arial", size=10)
        self.LEGEND_FONT = Font(name="Arial", size=9)

        self.LINE_WIDTH = 2
        self.MARKER_SIZE = 5

        self.DEFAULT_TITLE = "Gráfico"
        self.SHOW_LEGEND = True
        self.SHOW_VALUES = False
        self.SOLID_FILL= "FFFFFF"
        self.SOLID_FILLOP ="F4A460"
        self.SOLID_FILLOP2="2196F3"
