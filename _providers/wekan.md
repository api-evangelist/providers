---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 163
  human_in_the_loop: 1
  name: Wekan Agentic Access
  operation_count: 279
  slug: wekan-agentic-access
  summary_line: 279 operations · 163 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The Attachments API from WeKan — 15 operation(s) for attachments.
  name: WeKan Attachments API
  slug: wekan-attachments-api
- description: The AttachmentStorageSettings API from WeKan — 1 operation(s) for attachmentstoragesettings.
  name: WeKan Attachment Storage Settings API
  slug: wekan-attachmentstoragesettings-api
- description: The Boards API from WeKan — 33 operation(s) for boards.
  name: WeKan Boards API
  slug: wekan-boards-api
- description: The CardComments API from WeKan — 2 operation(s) for cardcomments.
  name: WeKan Card Comments API
  slug: wekan-cardcomments-api
- description: The Cards API from WeKan — 19 operation(s) for cards.
  name: WeKan Cards API
  slug: wekan-cards-api
- description: The Checklists API from WeKan — 2 operation(s) for checklists.
  name: WeKan Checklists API
  slug: wekan-checklists-api
- description: The Dependencies API from WeKan — 3 operation(s) for dependencies.
  name: WeKan Dependencies API
  slug: wekan-dependencies-api
- description: The Integrations API from WeKan — 3 operation(s) for integrations.
  name: WeKan Integrations API
  slug: wekan-integrations-api
- description: The Lists API from WeKan — 6 operation(s) for lists.
  name: WeKan Lists API
  slug: wekan-lists-api
- description: The Login API from WeKan — 2 operation(s) for login.
  name: WeKan Login API
  slug: wekan-login-api
- description: The Org API from WeKan — 3 operation(s) for org.
  name: WeKan Org API
  slug: wekan-org-api
- description: The Organizations API from WeKan — 3 operation(s) for organizations.
  name: WeKan Organizations API
  slug: wekan-organizations-api
- description: The Problems API from WeKan — 3 operation(s) for problems.
  name: WeKan Problems API
  slug: wekan-problems-api
- description: The Rules API from WeKan — 2 operation(s) for rules.
  name: WeKan Rules API
  slug: wekan-rules-api
- description: The Settings API from WeKan — 5 operation(s) for settings.
  name: WeKan Settings API
  slug: wekan-settings-api
- description: The Swimlanes API from WeKan — 4 operation(s) for swimlanes.
  name: WeKan Swimlanes API
  slug: wekan-swimlanes-api
- description: The Team API from WeKan — 3 operation(s) for team.
  name: WeKan Team API
  slug: wekan-team-api
- description: The Teams API from WeKan — 3 operation(s) for teams.
  name: WeKan Teams API
  slug: wekan-teams-api
- description: The Users API from WeKan — 8 operation(s) for users.
  name: WeKan Users API
  slug: wekan-users-api
- description: The Checklist Items API from WeKan — 2 operation(s) for checklist items.
  name: WeKan Checklist Items API
  slug: wekan-checklist-items-api
- description: The Custom Fields API from WeKan — 4 operation(s) for custom fields.
  name: WeKan Custom Fields API
  slug: wekan-custom-fields-api
- description: The Event Log API from WeKan — 3 operation(s) for event log.
  name: WeKan Event Log API
  slug: wekan-event-log-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/wekan/agentic-access/wekan-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/wekan-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/wekan/rules/wekan-rules.yml
  title: ''
  type: Spectral
  url: rules/wekan-rules.yml
- group: design
  href: https://artifacts.apis.io/wekan/vocabulary/wekan-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/wekan-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/wekan/data-model/wekan-data-model.yml
  title: ''
  type: DataModel
  url: data-model/wekan-data-model.yml
- group: design
  href: https://artifacts.apis.io/wekan/errors/wekan-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/wekan-problem-types.yml
- group: design
  href: https://artifacts.apis.io/wekan/conformance/wekan-conformance.yml
  title: ''
  type: Conformance
  url: conformance/wekan-conformance.yml
- group: other
  href: https://artifacts.apis.io/wekan/hosts/wekan-hosts.yml
  title: ''
  type: Hosts
  url: hosts/wekan-hosts.yml
- group: other
  href: https://artifacts.apis.io/wekan/vendors/wekan-vendors.yml
  title: ''
  type: Vendors
  url: vendors/wekan-vendors.yml
- group: auth
  href: https://artifacts.apis.io/wekan/authentication/wekan-authentication.yml
  title: ''
  type: Authentication
  url: authentication/wekan-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://wekan.github.io/
created: '2026-10-27'
description: WeKan is an open-source kanban board application that helps teams visualize work, manage tasks, and improve workflow efficiency. It offers features such as customizable boards, drag‑and‑drop cards, real‑time collaboration, and integrations with tools like GitHub and Trello. The project is community‑driven, with active development and a focus on flexibility and ease of use for both personal and enterprise environments.
layout: provider
modified: '2026-10-27'
name: WeKan
nav: Providers
network: true
overview: 'WeKan publishes 22 API contracts indexed on the [APIs.io](https://apis.io/) network, including Attachments API, Attachment Storage Settings API, Boards API, and 19 more. Tagged areas include Company.


  The WeKan catalog on APIs.io includes 1 Spectral governance ruleset.


  WeKan''s developer surface includes authentication and 9 more developer resources.'
random_paper: 6
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: WeKan API Rules
  rule_count: 9
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 3
  slug: wekan-rules
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 15
    catalog_earned: 30.8
    catalog_earned_first_party: 0.0
    catalog_gap: 84.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 37.5
    developer_ergonomics: 11.9
    discoverability: 44.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 18.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 22
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://apis.io/screenshots/wekan/wekan-2026-11-03T150113.png
security:
- kind: authentication
  name: Wekan Authentication
  slug: wekan-authentication
  summary_line: apiKey · 1 scheme
slug: wekan
tags:
- Company
website: https://wekan.github.io/
---
