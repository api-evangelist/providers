---
aid: symphony
url: >-

  https://raw.githubusercontent.com/api-search/financial/main/_apis/symphony/apis.md
apis:
  - aid: symphony:symphony-pod-api
    name: Symphony Pod API
    tags: []
    overlays:
      - url: overlays/pod-openapi-search.yml
        type: APIs.io Search
    description: |-

      The Symphony Pod API is used to build tools in order to manage and
      administer Symphony for your organization. 
  - aid: symphony:symphony-agent-api
    name: Symphony Agent API
    tags: []
    overlays:
      - url: overlays/agent-openapi-search.yml
        type: APIs.io Search
    description: |-

      The Symphony Agent is responsible for encryption and decryption of
      messages and content sent to and from a bot.
  - aid: symphony:symphony-authenticator-api
    name: Symphony Authenticator API
    tags: []
    overlays:
      - url: overlays/authenticator-openapi-search.yml
        type: APIs.io Search
    description: |-

      Tailor your portfolio exposures and risks using our hedging and
      optimization tools. Dynamically manage objectives and constraints while
      controlling for cost and tradability to meet your investment goals.
  - aid: symphony:symphony-community-connect-api
    name: Symphony Community Connect API
    tags: []
    overlays:
      - url: overlays/community-connect-openapi-search.yml
        type: APIs.io Search
    description: |-

      Access the full range of Goldman Sachs indices and basket products, or
      create bespoke solutions to tailor your own investment strategies. Design,
      create, and rebalance fully-customized, ready-to-trade basket solutions to
      express thematic and risk views.
  - aid: symphony:symphony-login-api
    name: Symphony Login API
    tags: []
    overlays:
      - url: overlays/login-openapi-search.yml
        type: APIs.io Search
    description: |-

      Programmatically manage your portfolio lifecycle from creation and update
      to scheduling reports with full control over visibility and sharing.
      Automate your portfolio workflow using our APIs - leaving you to focus on
      the alpha driving decisions.
  - aid: symphony:symphony-profile-manager-api
    name: Symphony Profile Manager API
    tags: []
    overlays:
      - url: overlays/profile-manager-openapi-search.yml
        type: APIs.io Search
    description: Profile Manager is a microservice to manage users profile and groups.
name: Symphony
tags: []
created: 2024/04/14
modified: '2024-07-03'
description: |-

  Streamline work and automate workflows with bots and apps. Build integrations
  from a simple hello world example to fully fledged financial integrations on
  Symphony.
maintainers:
  - FN: API Evangelist
    email: info@apievangelist.com
specificationVersion: '0.18'

---