---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.5
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 36
  human_in_the_loop: 1
  name: Guru Agentic Access
  operation_count: 77
  slug: guru-agentic-access
  summary_line: 77 operations · 36 acting · 1 human-in-the-loop
api_count: 18
apis:
- description: REST API for managing cards, collections, boards, board sections, folders, users, groups, tags, webhooks, analytics, and card verifications in Guru. Authentication uses HTTP Basic Auth with a user tok
  name: Guru REST API
  slug: rest-api
- description: The Analytics API from Guru — 2 operation(s) for analytics.
  name: Guru Analytics API
  slug: guru-analytics-api
- description: The Announcements API from Guru — 8 operation(s) for announcements.
  name: Guru Announcements API
  slug: guru-announcements-api
- description: The Answers API from Guru — 3 operation(s) for answers.
  name: Guru Answers API
  slug: guru-answers-api
- description: The CardComments API from Guru — 2 operation(s) for cardcomments.
  name: Guru CardComments API
  slug: guru-cardcomments-api
- description: The Cards API from Guru — 8 operation(s) for cards.
  name: Guru Cards API
  slug: guru-cards-api
- description: The CardVerifiers API from Guru — 3 operation(s) for cardverifiers.
  name: Guru CardVerifiers API
  slug: guru-cardverifiers-api
- description: The Collections API from Guru — 3 operation(s) for collections.
  name: Guru Collections API
  slug: guru-collections-api
- description: The Folders API from Guru — 10 operation(s) for folders.
  name: Guru Folders API
  slug: guru-folders-api
- description: The Groups API from Guru — 5 operation(s) for groups.
  name: Guru Groups API
  slug: guru-groups-api
- description: The Members API from Guru — 1 operation(s) for members.
  name: Guru Members API
  slug: guru-members-api
- description: The People API from Guru — 3 operation(s) for people.
  name: Guru People API
  slug: guru-people-api
- description: The Search API from Guru — 4 operation(s) for search.
  name: Guru Search API
  slug: guru-search-api
- description: The Tags API from Guru — 8 operation(s) for tags.
  name: Guru Tags API
  slug: guru-tags-api
- description: The Tasks API from Guru — 1 operation(s) for tasks.
  name: Guru Tasks API
  slug: guru-tasks-api
- description: The Templates API from Guru — 5 operation(s) for templates.
  name: Guru Templates API
  slug: guru-templates-api
- description: The TicketLinking API from Guru — 5 operation(s) for ticketlinking.
  name: Guru TicketLinking API
  slug: guru-ticketlinking-api
- description: The User API from Guru — 1 operation(s) for user.
  name: Guru User API
  slug: guru-user-api
artifact_total: 22
collections:
- collection_type: open
  name: Guru API
  slug: open-guru
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/guru-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/guru-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/guru-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/guruhq
- group: company
  title: ''
  type: Website
  url: https://www.getguru.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.getguru.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.getguru.com
- group: operate
  title: ''
  type: Help Center
  url: https://help.getguru.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getguru.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://app.getguru.com/signup
- group: operate
  title: ''
  type: Support
  url: https://help.getguru.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/guru-technologies-inc-
- group: agent
  title: ''
  type: LlmsText
  url: https://developer.getguru.com/llms.txt
created: '2026-05-11'
description: Guru is an AI-powered knowledge management and enterprise search platform that captures company knowledge into verifiable cards organized into collections, surfaces answers directly inside the apps employees already use (Slack, Chrome, Microsoft Teams, Salesforce), and uses AI to keep content trusted and up to date. The Guru REST API provides programmatic access to cards, collections, boards, users, groups, tags, analytics, and verifications. Authentication uses HTTP Basic Auth with a user token or Collection token generated by a Guru admin.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/guru.png
layout: provider
modified: '2026-05-11'
name: Guru
nav: Providers
network: true
overview: 'Guru publishes 17 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Announcements API, Answers API, and 14 more. Tagged areas include Knowledge Management, Enterprise Search, AI Knowledge Base, Internal Wiki, and Verified Knowledge.


  Guru''s developer surface includes authentication, documentation, pricing, signup flow, support, and 8 more developer resources.'
random_paper: 112
score:
  band: thin
  composite: 31.1
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 57.4
    developer_ergonomics: 32.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 31.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 17
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/guru/refs/heads/main/screenshots/guru-2026-06-20T182441.png
security:
- kind: authentication
  name: Guru Authentication
  slug: guru-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Guru Domain Security
  slug: guru-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: guru
tags:
- Knowledge Management
- Enterprise Search
- AI Knowledge Base
- Internal Wiki
- Verified Knowledge
- Workplace Productivity
website: https://www.getguru.com
---
