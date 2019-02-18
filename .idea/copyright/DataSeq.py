class DataSeq:
    WHITE = (255,255,255)
    RED = (0,0,255)
    BLACK = (0,0,0)
    YELLOW = (0,127,255)
    def __init__(self, Length, time_interval=1, sort_title="Figure", repeatition=False):
        pass
    def Getfigure(self):
        _bar_width = 5
        figure = np.full((self.length*_bar_width,self.length*_bar_width,3), 255,dtype=np.uint8)
        for i in range(self.length):
            val = self.data[i]
            figure[-1-val*_bar_width:, i*_bar_width:i*_bar_width+_bar_width] = self.GetColor(val, self.length)
        self._bar_width = _bar_width
        self.figure = figure
    def _set_figure(self, idx, val):
        min_col = idx*self._bar_width
        max_col = min_col+self._bar_width
        min_row = -1-val*self._bar_width
        self.figure[ : , min_col:max_col] = self.WHITE
        self.figure[ min_row: , min_col:max_col] = self.GetColor(val, self.length)
    def SetVal(self, idx, val):
        self.data[idx] = val
        self._set_figure(idx, val)

        self.Visualize((idx,))

    def Swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]
        self._set_figure(idx1, self.data[idx1])
        self._set_figure(idx2, self.data[idx2])

        self.Visualize((idx1, idx2))