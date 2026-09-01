---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Google Chat Agentic Access
  operation_count: 14
  slug: google-chat-agentic-access
  summary_line: 14 operations · 8 acting
api_count: 1
apis:
- description: The customEmojis API from Google Chat — 1 operation(s) for customemojis.
  name: Google Chat customEmojis API
  slug: google-chat-customemojis-api
- description: The Google Chat API API from Google Chat — 1 operation(s) for google chat api.
  name: Google Chat Google Chat API API
  slug: google-chat-google-chat-api-api
- description: The Members API from Google Chat — 1 operation(s) for members.
  name: Google Chat Members API
  slug: google-chat-members-api
- description: The Messages API from Google Chat — 1 operation(s) for messages.
  name: Google Chat Messages API
  slug: google-chat-messages-api
- description: The Reactions API from Google Chat — 1 operation(s) for reactions.
  name: Google Chat Reactions API
  slug: google-chat-reactions-api
- description: The Spaces API from Google Chat — 1 operation(s) for spaces.
  name: Google Chat Spaces API
  slug: google-chat-spaces-api
- description: The Spaces:setup API from Google Chat — 1 operation(s) for spaces:setup.
  name: Google Chat Spaces:setup API
  slug: google-chat-spaces-setup-api
artifact_total: 31
collections:
- collection_type: postman
  name: Google Chat customEmojis API
  slug: postman-google-chat-customemojis-api
- collection_type: postman
  name: Google Chat customEmojis Google Chat API API
  slug: postman-google-chat-google-chat-api-api
- collection_type: postman
  name: Google Chat customEmojis Members API
  slug: postman-google-chat-members-api
- collection_type: postman
  name: Google Chat customEmojis Messages API
  slug: postman-google-chat-messages-api
- collection_type: postman
  name: Google Chat customEmojis Reactions API
  slug: postman-google-chat-reactions-api
- collection_type: postman
  name: Google Chat customEmojis Spaces API
  slug: postman-google-chat-spaces-api
- collection_type: postman
  name: Google Chat customEmojis Spaces:setup API
  slug: postman-google-chat-spaces-setup-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Chat customEmojis API
  slug: open-google-chat-customemojis-api
- collection_type: open
  name: Google Chat customEmojis Google Chat API API
  slug: open-google-chat-google-chat-api-api
- collection_type: open
  name: Google Chat customEmojis Members API
  slug: open-google-chat-members-api
- collection_type: open
  name: Google Chat customEmojis Messages API
  slug: open-google-chat-messages-api
- collection_type: open
  name: Google Chat customEmojis Reactions API
  slug: open-google-chat-reactions-api
- collection_type: open
  name: Google Chat customEmojis Spaces API
  slug: open-google-chat-spaces-api
- collection_type: open
  name: Google Chat customEmojis Spaces:setup API
  slug: open-google-chat-spaces-setup-api
- collection_type: open
  name: Google Chat API
  slug: open-openapi
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-chat/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-chat-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-chat-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-chat-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/googleworkspace
- group: start
  title: ''
  type: Portal
  url: https://developers.google.com/workspace/chat
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/workspace/chat/api/guides
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: commercial
  title: ''
  type: Pricing
  url: https://workspace.google.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developers.google.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://www.google.com/appsstatus/dashboard/
- group: operate
  title: ''
  type: Support
  url: https://developers.google.com/workspace/chat/support
- group: company
  title: ''
  type: Blog
  url: https://workspaceupdates.googleblog.com/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/json-ld.jsonld
created: '2026-03-13'
description: The Google Chat API enables building Chat apps that integrate with Google Chat. It provides RESTful access to manage Chat spaces, memberships, messages, reactions, attachments, and custom emojis. The API supports creating conversational bots, automating messaging workflows, and managing organizational chat resources programmatically.
finops:
- name: Google Chat Finops
  service_category: API
  slug: google-chat-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/google-chat.png
jsonld:
- class_count: 4
  name: Json Ld Context
  property_count: 4
  slug: json-ld
layout: provider
modified: '2026-05-19'
name: Google Chat
nav: Providers
network: true
overview: 'Google Chat publishes 7 APIs on the [APIs.io](https://apis.io/) network, including customEmojis API, Google Chat API API, Members API, and 4 more. Tagged areas include Chat, Collaboration, Google, Google Workspace, and Messaging.


  The Google Chat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Google Chat''s developer surface includes developer portal, getting-started guide, authentication, pricing, support, engineering blog, and 9 more developer resources.'
plans:
- name: Google Chat Plans Pricing
  plan_count: 3
  slug: google-chat-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Google Chat Rate Limits
  slug: google-chat-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Google Chat API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: google-chat-jsonschema-spectral-rules
score:
  band: developing
  composite: 46.2
  coverage:
    artifact_dirs: 13
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 9.8
    contract_quality: 57.1
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 26.3
  previous_composite: 46.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-chat/refs/heads/main/screenshots/google-chat-2026-06-20T182033.png
security:
- kind: domain-security
  name: Google Chat Domain Security
  slug: google-chat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Chat Vulnerability Disclosure
  slug: google-chat-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-chat
tags:
- Chat
- Collaboration
- Google
- Google Workspace
- Messaging
- Spaces
website: https://developers.google.com/workspace/chat
---
