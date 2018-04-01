class PageResult:
    pageNo = 0
    pageSize = 10
    totalCounts = 0
    totalPages = 1
    contents = None

    def __init__(self, pageNo=0, pageSize=10, totalCounts=0, totalPages=1, contents=None):
        self.pageNo = pageNo
        self.pageSize = pageSize
        self.totalCounts = totalCounts
        self.totalPages = totalPages
        self.contents = contents