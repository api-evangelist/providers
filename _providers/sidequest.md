---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
api_count: 1
apis:
- baseURL: https://api.sidequestvr.com
  baseurl_source: declared
  description: The Apps API from SideQuest — 1 operation(s) for apps.
  name: SideQuest Apps API
  slug: sidequest-apps-api
- baseURL: https://api.sidequestvr.com
  baseurl_source: declared
  description: The Developers API from SideQuest — 1 operation(s) for developers.
  name: SideQuest Developers API
  slug: sidequest-developers-api
- baseURL: https://api.sidequestvr.com
  baseurl_source: declared
  description: The OAuth2 API from SideQuest — 3 operation(s) for oauth2.
  name: SideQuest OAuth2 API
  slug: sidequest-oauth2-api
- baseURL: https://api.sidequestvr.com
  baseurl_source: declared
  description: The Users API from SideQuest — 2 operation(s) for users.
  name: SideQuest Users API
  slug: sidequest-users-api
- baseURL: https://api.sidequestvr.com
  baseurl_source: declared
  description: The UsersApps API from SideQuest — 1 operation(s) for usersapps.
  name: SideQuest UsersApps API
  slug: sidequest-usersapps-api
artifact_total: 14
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SideQuest Apps API
  slug: open-sidequest-apps-api
- collection_type: open
  name: SideQuest Apps Developers API
  slug: open-sidequest-developers-api
- collection_type: open
  name: SideQuest Apps OAuth2 API
  slug: open-sidequest-oauth2-api
- collection_type: open
  name: SideQuest Apps Users API
  slug: open-sidequest-users-api
- collection_type: open
  name: SideQuest Apps UsersApps API
  slug: open-sidequest-usersapps-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.sidequestvr.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/sidequest-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/sidequest-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sidequest-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sidequest-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sidequest-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sidequest-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sidequest-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sidequest-data-model.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/sidequest-openapi-overlay.yaml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sidequest-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sidequest-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/sidequest-packages.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sidequest-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://api.sidequestvr.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://sidequestvr.com/developers
created: '2026-07-17'
description: SideQuest is a VR content-discovery platform and independent app store for Meta Quest, PCVR, Pico, Magic Leap and WebXR headsets — the home of sideload-only, early-access and indie VR apps and games, plus tools to help users get more from their VR headset. SideQuest operates a public REST API (api.sidequestvr.com) for browsing the app catalog and reading user profiles and achievements, secured with OAuth 2.0 bearer tokens and a device-style short-code login. Backed by GV.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sidequest.png
layout: provider
modified: '2026-07-21'
name: SideQuest
nav: Providers
network: true
overview: 'SideQuest publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Apps API, Developers API, OAuth2 API, and 2 more. Tagged areas include Company, Consumer, Virtual Reality, VR, and XR.


  SideQuest''s developer surface includes authentication, documentation, and 15 more developer resources.'
random_paper: 17
scopes:
- name: Sidequest Scopes
  scope_count: 0
  slug: sidequest-scopes
  summary_line: OAuth 2.0 · no documented scopes
screenshot: https://raw.githubusercontent.com/api-evangelist/sidequest/refs/heads/main/screenshots/sidequest-2026-09-02T155400.png
security:
- kind: authentication
  name: Sidequest Authentication
  slug: sidequest-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sidequest Domain Security
  slug: sidequest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: sidequest
tags:
- Company
- Consumer
- Virtual Reality
- VR
- XR
- Gaming
- App Store
- Developers
website: https://www.sidequestvr.com/
---
