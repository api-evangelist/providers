---
aid: youtube
url: https://raw.githubusercontent.com/api-search/videos/main/_apis/youtube/apis.md
apis:
  - aid: youtube:youtube-activities-api
    name: Youtube Activities API
    tags:
      - Videos
      - Activities
    properties:
      - url: https://developers.google.com/youtube/v3/docs/activities/list
        type: Documentation
    description: Managing Youtube activities.
  - aid: youtube:youtube-channels-api
    name: Youtube Channels API
    tags:
      - Videos
      - Channels
    properties:
      - url: https://developers.google.com/youtube/v3/docs/channels/list
        type: Documentation
    description: Managing Youtube channels.
  - aid: youtube:youtube-comments-api
    name: Youtube Comments API
    tags:
      - Videos
      - Comments
    properties:
      - url: https://developers.google.com/youtube/v3/docs/comments/list
        type: Documentation
    description: Managing Youtube comments.
  - aid: youtube:youtube-comment-threads-api
    name: Youtube Comment Threads API
    tags:
      - Videos
      - Comment Threads
    properties:
      - url: https://developers.google.com/youtube/v3/docs/commentThreads/list
        type: Documentation
    description: Managing Youtube comment threads.
  - aid: youtube:youtube-playlists-api
    name: Youtube Playlists API
    tags:
      - Videos
      - Playlists
    properties:
      - url: https://developers.google.com/youtube/v3/docs/playlists/list
        type: Documentation
    description: Managing Youtube playlists.
  - aid: youtube:youtube-playlist-items-api
    name: Youtube Playlist Items API
    tags:
      - Videos
      - Playlist Items
    properties:
      - url: https://developers.google.com/youtube/v3/docs/playlistItems/list
        type: Documentation
    description: Managing Youtube playlist items.
  - aid: youtube:youtube-search-api
    name: Youtube Search API
    tags:
      - Videos
      - Search
    properties:
      - url: https://developers.google.com/youtube/v3/docs/search/list
        type: Documentation
    description: Managing Youtube search.
  - aid: youtube:youtube-subscriptions-api
    name: Youtube Subscriptions API
    tags:
      - Videos
      - Subscriptions
    properties:
      - url: https://developers.google.com/youtube/v3/docs/subscriptions/list
        type: Documentation
    description: Managing Youtube subscriptions.
  - aid: youtube:youtube-videos-api
    name: Youtube Videos API
    tags:
      - Videos
    properties:
      - url: https://developers.google.com/youtube/v3/docs/videos/list
        type: Documentation
    description: Managing Youtube videos.
name: Youtube
tags:
  - Videos
common:
  - url: https://developers.google.com/youtube/v3
    name: Portal
    type: Portal
  - url: https://developers.google.com/youtube/v3/getting-started
    name: Guides
    type: Guides
  - url: https://developers.google.com/youtube/v3/code_samples
    name: Samples
    type: Samples
  - url: https://developers.google.com/youtube/v3/support
    name: Support
    type: Support
  - url: https://github.com/youtube/api-samples
    name: GitHubRepository
    type: GitHubRepository
  - url: https://www.youtube.com/user/YouTubeDev
    name: Videos
    type: Videos
  - url: https://developers.google.com/youtube/terms/api-services-terms-of-service
    name: Terms of Service
    type: TermsOfService
  - url: https://developers.google.com/youtube/terms/branding-guidelines
    name: Branding
    type: Branding
  - url: https://developers.google.com/youtube/terms/revision-history
    name: Change Log
    type: ChangeLog
  - name: Plans
    type: Plans
    data:
      - id: free
        name: Free
        description: Youtube has only free tier.
        entries:
          - geo: US
            unit: 1
            label: User
            limit: 1
            price: Free
            metric: user
            timeFrame: month
            description: Free tier.
  - name: Rate Limits
    url: https://developers.google.com/youtube/v3/determine_quota_cost
    type: Rate Limits
created: '2025-07-29'
modified: '2025-07-29'
description: |-
  The Youtube API provides the ability to retrieve feeds related to videos,
  users, and playlists. It also provides the ability to manipulate these feeds,
  such as creating new playlists, adding videos as favorites, and sending
  messsages. The API is also able to upload videos.
maintainers:
  - FN: API Evangelist
    url: https://apievangelist.com
    email: info@apievangelist.com
specificationVersion: '0.20'
---