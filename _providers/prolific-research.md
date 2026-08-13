---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
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
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Prolific Research Agentic Access
  operation_count: 49
  slug: prolific-research-agentic-access
  summary_line: 49 operations · 25 acting
api_count: 10
apis:
- description: Bulk bonus payments to participants.
  name: Prolific Bonuses API
  slug: prolific-research-bonuses-api
- description: Demographic and screening requirements and eligibility counts.
  name: Prolific Filters API
  slug: prolific-research-filters-api
- description: Event webhook subscriptions and signing secrets.
  name: Prolific Hooks API
  slug: prolific-research-hooks-api
- description: Communicate with participants.
  name: Prolific Messages API
  slug: prolific-research-messages-api
- description: Saved, dynamic groups of participant IDs used as allowlist/blocklist filters.
  name: Prolific Participant Groups API
  slug: prolific-research-participant-groups-api
- description: Organize studies within a workspace.
  name: Prolific Projects API
  slug: prolific-research-projects-api
- description: Create, publish, and manage research studies.
  name: Prolific Studies API
  slug: prolific-research-studies-api
- description: Review, approve, reject, and return participant submissions.
  name: Prolific Submissions API
  slug: prolific-research-submissions-api
- description: Authenticated account and user identity.
  name: Prolific Users API
  slug: prolific-research-users-api
- description: Top-level containers that hold projects, fund studies, and scope teams.
  name: Prolific Workspaces API
  slug: prolific-research-workspaces-api
artifact_total: 17
collections:
- collection_type: open
  name: Prolific API
  slug: open-prolific-research
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/prolific-research-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/prolific-research-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/prolific-research-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/prolific-oss
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prolific-com
- group: company
  title: ''
  type: Website
  url: https://www.prolific.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.prolific.com
- group: commercial
  title: ''
  type: Plans
  url: plans/prolific-research-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/prolific-research-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/prolific-research-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.prolific.com/resources/blog
created: '2026-07-04'
description: Prolific is an online research participant recruitment platform that connects researchers and AI teams with a large, vetted pool of human participants for surveys, experiments, and data annotation. The Prolific API is a versioned REST interface (https://api.prolific.com/api/v1) authenticated with an API token that lets researchers programmatically create and publish studies, review and approve submissions, manage participant groups, projects and workspaces, apply demographic filters and requirements, pay bonuses, message participants, and subscribe to event webhooks (hooks).
finops:
- name: Prolific Research Finops
  service_category: Research and Human Data
  slug: prolific-research-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prolific-research.png
layout: provider
modified: '2026-07-04'
name: Prolific
nav: Providers
network: true
overview: 'Prolific publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Bonuses API, Filters API, Hooks API, and 7 more. Tagged areas include Research, Participant Recruitment, Surveys, Human Data, and Crowdsourcing.


  Prolific''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Prolific Research Plans Pricing
  plan_count: 3
  slug: prolific-research-plans-pricing
random_paper: 66
rate_limits:
- limit_count: 5
  name: Prolific Research Rate Limits
  slug: prolific-research-rate-limits
score:
  band: thin
  composite: 38.7
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.2
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Prolific Research Authentication
  slug: prolific-research-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prolific Research Domain Security
  slug: prolific-research-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: prolific-research
tags:
- Research
- Participant Recruitment
- Surveys
- Human Data
- Crowdsourcing
- Data Annotation
- AI Training
website: https://www.prolific.com
---
