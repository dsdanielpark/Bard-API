class DraftCitation:
    """Github source
    [[909, 1095, ['', 'edelahoz/Introduction-to-Python                 ', '', '', '', None, None, '', False, '', '', '', '', '', '',   ''], 1, 100, None, [1]],
    [940, 1139,  ['', 'Engr-Asad-Hussain/oop                           ', '', '', '', None, None, '', False, '', '', '', '', '', '',   ''], 1, 100, None, [1]],
    [953, 1166,  ['', 'TeknikhogskolanGothenburg/PGBPYH21_Programmering', '', '', '', None, None, '', False, '', '', '', '', '', '',   ''], 1, 100, None, [1]]]

    Wiki source
    [[284, 425, ['http://en.wikipedia.org/wiki/Jill_Biden', '          ', '', None, '', None, None, '', False, '', '', '', '', '', '', ''], 1, 1  , None, [1, 'normal_citation_datasets']],
     [196, 411, ['https://en.wikipedia.org/wiki/Jill_Biden#:~:text=Jill%20Tracy%20Jacobs%20was%20born,II%20who%20used%20the%20G.I.', '', '', '', '', None, None, '', False, '', '', '', '', '', '', ''], 2, 2, None, [1, 'normal_citation_datasets']]]]

     [None, None, ['https://en.wikipedia.org/wiki/Te%27omim_Cave'], 3]
    """

    def __init__(self, input_list: list, text: str):
        self._input_list = input_list
        self.span: tuple[int, int] = self._input_list[0], self._input_list[1]
        if self.span[0] is None or self.span[1] is None:
            self.text = ""
        else:
            self.text: str = text[self.span[0] : self.span[1]]

    @property
    def source_path(self) -> str:
        return self._input_list[2][1] if len(self._input_list[2]) > 1 else ""

    @property
    def source_full(self) -> str:
        return self._input_list[2][0]

    @property
    def source_dataset(self) -> list:
        if len(self._input_list) < 5:
            return []
        return self._input_list[6]

    def __str__(self) -> str:
        return self.source_full if self.source_full else self.source_path
