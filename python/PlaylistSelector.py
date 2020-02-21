import  sys
from    utils.timing import timeit_run
from    utils.io     import display_result

class Song:
    def __init__(self, title: str, duration: float):
        self._title = title
        self._duration = duration

    @property
    def title(self) -> str:
        return self._title

    @property
    def duration(self) -> float:
        return self._duration

    def __str__(self) -> str:
        return f'"{self.title}" - {self.duration} secs'

    def __repr__(self) -> str:
        return str(self)

def select_two_songs_v1(playlist: list, total_duration: float) -> list:
    ans = list()
    for i, s0 in enumerate(playlist):
        for s1 in playlist[i + 1:]:
            if s0.duration + s1.duration == total_duration:
                ans.append((s0, s1))
    return ans

def select_two_songs_v2(playlist: list, total_duration: float) -> list:
    ans = list()
    i = 0
    while(i < len(playlist)):
        j = i + 1
        while (j < len(playlist)):
            if playlist[i].duration + playlist[j].duration == total_duration:
                ans.append((playlist[i], playlist[j]))
            j += 1
        i += 1
    return ans

def select_two_songs_v3(playlist: list, total_duration: float) -> list:
    ans = list()
    visited = dict()
    for s in playlist:
        remaining_duration = total_duration - s.duration
        if remaining_duration in visited:
            ans.append((visited[remaining_duration], s))
        visited[s.duration] = s
    return ans



def main() -> int:
    playlist_small = [
        Song('A', 5.5), Song('B', 4), Song('C', 1), Song('D', 2),
        Song('E', 7), Song('F', 4.5), Song('G', 3)
    ]

    print ("Small Test")
    display_result(select_two_songs_v1, playlist_small, 10.0)
    display_result(select_two_songs_v2, playlist_small, 10.0)
    display_result(select_two_songs_v3, playlist_small, 10.0)

    print ("\nLarge test")
    playlist_large = playlist_small * 500
    timeit_run(select_two_songs_v1, playlist_large, 10.0)
    timeit_run(select_two_songs_v2, playlist_large, 10.0)
    timeit_run(select_two_songs_v3, playlist_large, 10.0)

    return 0

if __name__ == '__main__': sys.exit(main())




