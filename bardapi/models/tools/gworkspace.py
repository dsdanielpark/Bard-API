from enum import Enum


class GoogleWorkspaceContentKind(Enum):
    UNKNOWN = 0
    EMAIL = 1
    FILE = 2
    DOCUMENT = 3
    PDF = 4
    SPREADSHEET = 5


class GoogleWorkspaceContent:
    # [[1], 'https://mail.google.com/mail/u/0/#all/18ad29e935cf6dc3',
    # 'Start your journey to becoming an AI expert today!', ['18ad29e935cf6dc3'],
    # 'Tuesday, 26 September 2023 19:52 CEST', 'Stanford University', [1695750721]]

    # [[3], 'https://docs.google.com/document/d/1pS5RTC2PSVn02lGOOAtaEg5U9M4_Ss_eoqkb2msO-Yo',
    # 'CV (Andrew Matuk)', ['1pS5RTC2PSVn02lGOOAtaEg5U9M4_Ss_eoqkb2msO-Yo', 147325],
    # 'Friday, 28 July 2023 11:29 CEST', 'Andrew Me', [1690536542, 363000000]]
    def __init__(self, input_list: list):
        self._input_list = input_list

    @property
    def kind(self) -> GoogleWorkspaceContentKind:
        return (
            GoogleWorkspaceContentKind(self._input_list[0][0])
            if self._input_list[0] < 5
            else GoogleWorkspaceContentKind.UNKNOWN
        )

    def icon(self) -> str:
        di = {
            GoogleWorkspaceContentKind.UNKNOWN: "https://drive-thirdparty.googleusercontent.com/64/type/application/vnd.google-apps.unknown",
            GoogleWorkspaceContentKind.EMAIL: "https://www.gstatic.com/lamda/images/default_email_avatar_7fc85bbd3d2f35d5bd091.svg",
            GoogleWorkspaceContentKind.FILE: "https://drive-thirdparty.googleusercontent.com/64/type/application/vnd.google-apps.file",
            GoogleWorkspaceContentKind.DOCUMENT: "https://drive-thirdparty.googleusercontent.com/64/type/application/vnd.google-apps.document",
            GoogleWorkspaceContentKind.PDF: "https://drive-thirdparty.googleusercontent.com/64/type/application/pdf",
            GoogleWorkspaceContentKind.SPREADSHEET: "https://drive-thirdparty.googleusercontent.com/64/type/application/vnd.google-apps.spreadsheet",
        }
        return di[self.kind]

    @property
    def url(self) -> str:
        return self._input_list[1]

    @property
    def title(self) -> str:
        return self._input_list[2]

    @property
    def id(self) -> str:
        return self._input_list[3][0]

    @property
    def date(self) -> str:
        return self._input_list[4]

    @property
    def author(self) -> str:
        return self._input_list[5]

    @property
    def timestamp_seconds(self) -> [int]:
        return self._input_list[6]

    def __str__(self) -> str:
        return self.title
