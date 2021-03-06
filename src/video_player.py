"""A video player class."""

from .video_library import VideoLibrary
import random

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video = {}
        self.previous = {}
        self.paused = {}
        self.playlist = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        #sorts list in alphabetical order by video title
        video_list = sorted(self._video_library.get_all_videos(), key=lambda video: video.title)
        print("Here's a list of all available videos:")

        for video in video_list:
            #formatted output
            print(f"{video.title} ({video.video_id}) [{' '.join(video.tags)}]")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        self.video = self._video_library.get_video(video_id)

        if self.video and not self.previous:
            self.previous = self.video
            self.paused = {}
            print(f"Playing video: {self.video.title}")
        elif self.video and self.previous:
            self.video = self.previous
            self.stop_video()
            self.video = self._video_library.get_video(video_id)
            self.previous = self.video
            self.paused = {}
            print(f"Playing video: {self.video.title}")
        else:
            print("Cannot play video: Video does not exist")
        
    def stop_video(self):
        """Stops the current video."""
        
        if self.video:
            print(f"Stopping video: {self.video.title}")
            self.video = {}
            self.previous = {}
            self.paused = {}
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""

        num_videos = len(self._video_library.get_all_videos())
        random_index = random.randrange(0,num_videos)
        video_list = self._video_library.get_all_videos()

        self.video = video_list[random_index]

        if self.video and not self.previous:
            self.previous = self.video
            self.paused = {}
            print(f"Playing video: {self.video.title}")
        elif self.video and self.previous:
            self.video = self.previous
            self.stop_video()
            self.video = video_list[random_index]
            self.previous = self.video
            self.paused = {}
            print(f"Playing video: {self.video.title}")

    def pause_video(self):
        """Pauses the current video."""
        if self.paused:
            print(f"Video already paused: {self.video.title}")
        elif self.video and not self.paused:
            print(f"Pausing video: {self.video.title}")
            self.paused = self.video
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        if self.video and self.paused:
            print(f"Continuing video: {self.video.title}")
        elif self.video and not self.paused:
            print(f"Cannot continue video: Video is not paused")
        else:
            print(f"Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""

        if self.video and not self.paused:
            print(f"Currently playing: {self.video.title} ({self.video.video_id}) [{' '.join(self.video.tags)}]")
        elif self.video and self.paused:
            print(f"Currently playing: {self.video.title} ({self.video.video_id}) [{' '.join(self.video.tags)}] - PAUSED")
        else: 
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if self.playlist != playlist_name:
            self.playlist = playlist_name
            print(f"Successfully created new playlist: {self.playlist}")
        elif self.playlist == playlist_name:
            print("Cannot create playlist: A playlist with the same name already exists")


    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        self.video = self._video_library.get_video(video_id)
        self.playlist = {self.video}
        print(f"Added video to {playlist_name}: {self.video.title}")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
