---
aid: telegram
name: Telegram
description: Telegram is a cloud-based instant messaging and voice-over-IP service that provides a comprehensive Bot API for developers to build bots, automate workflows, send notifications, and create interactive experiences on the Telegram platform. The platform supports text messages, media sharing, payments, inline keyboards, inline queries, webhooks, and live location sharing.
type: Index
position: Consumer
access: 3rd-Party
image: https://telegram.org/img/t_logo.png
tags:
  - Bots
  - Chat
  - Messaging
  - Notifications
  - Payments
  - Telegram
created: '2025-02-12'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/telegram/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: telegram:telegram-bot-api
    name: Telegram Bot API
    description: The Telegram Bot API is an HTTP-based interface for building bots on Telegram. Bots are small programs that run inside Telegram and can do virtually anything — teach, play, search, broadcast, remind, connect, integrate with other services, or serve as front ends for businesses and services of all kinds. The Bot API provides methods for sending messages, managing chats, handling payments, working with stickers, managing webhooks, and much more.
    humanURL: https://core.telegram.org/bots/api
    baseURL: https://api.telegram.org/bot{token}
    version: '9.5'
    tags:
      - Bot Development
      - Bots
      - Chat Management
      - Messaging
      - Notifications
      - Payments
      - Telegram
      - Webhooks
    properties:
      - type: Documentation
        url: https://core.telegram.org/bots/api
      - type: GettingStarted
        url: https://core.telegram.org/bots
      - type: OpenAPI
        url: openapi/telegram-bot-openapi.yml
      - type: GitHubRepository
        url: https://github.com/tdlib/telegram-bot-api
      - type: Authentication
        url: https://core.telegram.org/bots/api#authorizing-your-bot
      - type: Changelog
        url: https://core.telegram.org/bots/api-changelog
      - type: FAQ
        url: https://core.telegram.org/bots/faq
    contact:
      - type: Support
        url: https://t.me/BotSupport
      - type: GitHub
        url: https://github.com/tdlib/telegram-bot-api
  - aid: telegram:telegram-tdlib
    name: Telegram TDLib (Telegram Database Library)
    description: TDLib is a cross-platform, fully functional Telegram client library for third-party developers. TDLib takes care of all network implementation details, encryption and local data storage, allowing developers to build custom Telegram clients. It is open source, written in C++, and compatible with virtually any programming language through bindings.
    humanURL: https://core.telegram.org/tdlib
    baseURL: https://core.telegram.org/tdlib
    version: '1.8'
    tags:
      - Client Library
      - Cross-Platform
      - MTProto
      - Open Source
      - Telegram
    properties:
      - type: Documentation
        url: https://core.telegram.org/tdlib
      - type: GettingStarted
        url: https://core.telegram.org/tdlib/getting-started
      - type: GitHubRepository
        url: https://github.com/tdlib/td
    contact:
      - type: GitHub
        url: https://github.com/tdlib/td
common:
  - type: Authentication
    url: https://core.telegram.org/bots/api#authorizing-your-bot
  - type: Terms of Service
    url: https://telegram.org/tos
  - type: Privacy Policy
    url: https://telegram.org/privacy
  - type: Developer Portal
    url: https://core.telegram.org
  - type: Status
    url: https://downdetector.com/status/telegram/
  - type: Blog
    url: https://telegram.org/blog
  - type: GitHub
    url: https://github.com/tdlib
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
