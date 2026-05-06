---
aid: open-podcast-api-open-podcast-api
name: Open Podcast API
description: The Open Podcast API is an initiative aiming to provide a feature-complete synchronization API specification for podcast (web) apps and user-focused servers. The specification covers synchronization of subscriptions, listening progress, favorites, queues, and device state across compliant clients and self-hosted servers, with the goal of giving listeners portable control of their podcast data.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Audio
  - Episodes
  - Open Standards
  - Podcasts
  - Subscriptions
  - Sync
created: '2025-05-02'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/open-podcast-api-open-podcast-api/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: open-podcast-api-open-podcast-api:authentication-api
    name: Open Podcast Authentication API
    description: Authenticate users against an Open Podcast compliant server, establishing the session used for subsequent subscription, action, and device endpoints.
    humanURL: https://openpodcastapi.org/
    tags:
      - Authentication
      - Sessions
    properties:
      - type: Documentation
        url: https://openpodcastapi.org/
  - aid: open-podcast-api-open-podcast-api:subscriptions-api
    name: Open Podcast Subscriptions API
    description: Synchronize a user's podcast subscriptions across clients, including adding and removing feed URLs and retrieving the current subscription set per device.
    humanURL: https://openpodcastapi.org/
    tags:
      - Feeds
      - Subscriptions
      - Sync
    properties:
      - type: Documentation
        url: https://openpodcastapi.org/
  - aid: open-podcast-api-open-podcast-api:episode-actions-api
    name: Open Podcast Episode Actions API
    description: Record and synchronize per-episode listening actions such as play, pause, download, delete, and flag, including timestamp and position metadata.
    humanURL: https://openpodcastapi.org/
    tags:
      - Episodes
      - Listening Progress
      - Sync
    properties:
      - type: Documentation
        url: https://openpodcastapi.org/
  - aid: open-podcast-api-open-podcast-api:devices-api
    name: Open Podcast Devices API
    description: Register and manage the devices a user syncs from, allowing servers to track per-device subscription state and last-sync timestamps.
    humanURL: https://openpodcastapi.org/
    tags:
      - Devices
      - Registration
      - Sync
    properties:
      - type: Documentation
        url: https://openpodcastapi.org/
  - aid: open-podcast-api-open-podcast-api:favorites-api
    name: Open Podcast Favorites API
    description: Synchronize a user's favorited episodes across clients so that liked or starred items remain consistent regardless of which app or device the user is on.
    humanURL: https://openpodcastapi.org/
    tags:
      - Favorites
      - Sync
    properties:
      - type: Documentation
        url: https://openpodcastapi.org/
  - aid: open-podcast-api-open-podcast-api:queue-api
    name: Open Podcast Queue API
    description: Synchronize the user's playback queue (up-next list) across clients, including ordering, additions, and removals of episodes.
    humanURL: https://openpodcastapi.org/
    tags:
      - Playback
      - Queue
      - Sync
    properties:
      - type: Documentation
        url: https://openpodcastapi.org/
common:
  - type: Website
    url: https://openpodcastapi.org/
  - type: Documentation
    url: https://openpodcastapi.org/
  - type: GitHub Organization
    url: https://github.com/openpodcastapi
  - type: Discussions
    url: https://github.com/orgs/openpodcastapi/discussions
  - type: Matrix Chat
    url: https://matrix.to/#/#openpodcastapi:matrix.org
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
