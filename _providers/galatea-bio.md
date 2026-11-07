---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 55
  human_in_the_loop: 1
  name: Galatea Bio Agentic Access
  operation_count: 99
  slug: galatea-bio-agentic-access
  summary_line: 99 operations · 55 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The auth API from Galatea Bio — 5 operation(s) for auth.
  name: Galatea Bio Auth API
  slug: galatea-bio-auth-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The credit API from Galatea Bio — 14 operation(s) for credit.
  name: Galatea Bio Credit API
  slug: galatea-bio-credit-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The dashboard API from Galatea Bio — 7 operation(s) for dashboard.
  name: Galatea Bio Dashboard API
  slug: galatea-bio-dashboard-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The data API from Galatea Bio — 12 operation(s) for data.
  name: Galatea Bio Data API
  slug: galatea-bio-data-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The exec API from Galatea Bio — 11 operation(s) for exec.
  name: Galatea Bio Exec API
  slug: galatea-bio-exec-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The internal API from Galatea Bio — 4 operation(s) for internal.
  name: Galatea Bio Internal API
  slug: galatea-bio-internal-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The notification API from Galatea Bio — 3 operation(s) for notification.
  name: Galatea Bio Notification API
  slug: galatea-bio-notification-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The organizations API from Galatea Bio — 13 operation(s) for organizations.
  name: Galatea Bio Organizations API
  slug: galatea-bio-organizations-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The statistics API from Galatea Bio — 2 operation(s) for statistics.
  name: Galatea Bio Statistics API
  slug: galatea-bio-statistics-api
- baseURL: https://api.galatea.bio/api/v1
  baseurl_source: declared
  description: The users API from Galatea Bio — 8 operation(s) for users.
  name: Galatea Bio Users API
  slug: galatea-bio-users-api
artifact_total: 22
asyncapis:
- description: ''
  name: Galatea Bio Octopod Webhooks
  slug: galatea-bio-octopod-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/galatea-bio/agentic-access/galatea-bio-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/galatea-bio-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://galatea.bio/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.galatea.bio/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.galatea.bio/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.galatea.bio/#api-reference-contents
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.galatea.bio/#recipes-contents
- group: start
  title: ''
  type: Login
  url: https://app.galatea.bio/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GalateaBio
- group: auth
  title: ''
  type: Compliance
  url: https://galatea.bio/life-sciences
- group: auth
  href: https://artifacts.apis.io/galatea-bio/authentication/galatea-bio-authentication.yml
  title: ''
  type: Authentication
  url: authentication/galatea-bio-authentication.yml
- group: design
  href: https://artifacts.apis.io/galatea-bio/conventions/galatea-bio-conventions.yml
  title: ''
  type: Conventions
  url: conventions/galatea-bio-conventions.yml
- group: design
  href: https://artifacts.apis.io/galatea-bio/errors/galatea-bio-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/galatea-bio-problem-types.yml
- group: design
  href: https://artifacts.apis.io/galatea-bio/data-model/galatea-bio-data-model.yml
  title: ''
  type: DataModel
  url: data-model/galatea-bio-data-model.yml
- group: design
  href: https://artifacts.apis.io/galatea-bio/lifecycle/galatea-bio-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/galatea-bio-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/galatea-bio/conformance/galatea-bio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/galatea-bio-conformance.yml
- group: design
  href: https://artifacts.apis.io/galatea-bio/asyncapi/galatea-bio-octopod-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/galatea-bio-octopod-webhooks.yml
- group: start
  href: https://artifacts.apis.io/galatea-bio/sandbox/galatea-bio-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/galatea-bio-sandbox.yml
- group: build
  href: https://artifacts.apis.io/galatea-bio/packages/galatea-bio-packages.yml
  title: ''
  type: Packages
  url: packages/galatea-bio-packages.yml
- group: build
  href: https://artifacts.apis.io/galatea-bio/packages/galatea-bio-packages.yml
  title: ''
  type: SDKs
  url: packages/galatea-bio-packages.yml
- group: build
  href: https://artifacts.apis.io/galatea-bio/cli/galatea-bio-cli.yml
  title: ''
  type: CLI
  url: cli/galatea-bio-cli.yml
- group: agent
  href: https://artifacts.apis.io/galatea-bio/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/galatea-bio/llms/galatea-bio-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/galatea-bio-llms.txt
- group: other
  href: https://artifacts.apis.io/galatea-bio/overlays/galatea-bio-octopod-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/galatea-bio-octopod-overlay.yaml
- group: operate
  href: https://artifacts.apis.io/galatea-bio/rate-limits/galatea-bio-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/galatea-bio-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/galatea-bio/plans/galatea-bio-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/galatea-bio-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/galatea-bio/security/galatea-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/galatea-bio-domain-security.yml
created: '2026-08-16'
description: Galatea Bio is a Miami Lakes, Florida genomics company that operates a CLIA-CMS certified, CAP-accredited high-complexity clinical laboratory alongside the Biobank of the Americas, working to close the ancestry gap in genomic medicine by sequencing populations under-represented in existing reference panels. Its developer surface is the Octopod Ancestry API, a REST API at https://api.galatea.bio/api/v1 that lets clinical and research customers upload genomic source files (VCF) over HTTPS or SFTP, submit execution orders against named analysis models including the StrataRisk polygenic risk score, organize work with tags, receive HMAC-signed webhook deliveries when a file validates or an order completes, and download ancestry, PRS, JSON and PDF report results. The same API also exposes organization administration, SFTP user and SSH key management, credit/tariff accounting, dashboards and statistics.
image: https://galatea.bio/favicon.png
layout: provider
modified: '2026-08-16'
name: Galatea Bio
nav: Providers
network: true
overview: 'Galatea Bio publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Credit API, Dashboard API, and 7 more. Tagged areas include Genomics, Bioinformatics, Ancestry, Precision Medicine, and polygenic-risk-score.


  The Galatea Bio catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Galatea Bio''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, CLI, and 20 more developer resources.'
plans:
- name: Galatea Bio Plans Pricing
  plan_count: 0
  slug: galatea-bio-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Galatea Bio Rate Limits
  slug: galatea-bio-rate-limits
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Galatea Bio API Rules
  rule_count: 48
  severity_counts:
    error: 38
    hint: 0
    info: 5
    warn: 5
  slug: galatea-bio-rules
score:
  band: thin
  composite: 33.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 6.6
    contract_governance: 31.8
    contract_quality: 54.5
    developer_ergonomics: 35.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 33.8
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/galatea-bio/galatea-bio-2026-08-17T080949.png
security:
- kind: authentication
  name: Galatea Bio Authentication
  slug: galatea-bio-authentication
  summary_line: apiKey/http-bearer · 1 scheme
- kind: domain-security
  name: Galatea Bio Domain Security
  slug: galatea-bio-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: Authenticate against the Galatea Bio Octopod Ancestry API
  slug: galatea-bio-authenticate
- name: Configure and verify Octopod webhook deliveries
  slug: galatea-bio-configure-webhooks
- name: Request and download PRS and ancestry PDF reports
  slug: galatea-bio-request-pdf-reports
- name: Retrieve ancestry and PRS results for a completed order
  slug: galatea-bio-retrieve-results
- name: Upload a genomic file and submit an analysis order
  slug: galatea-bio-upload-and-submit-order
slug: galatea-bio
tags:
- Genomics
- Bioinformatics
- Ancestry
- Precision Medicine
- polygenic-risk-score
- Clinical Laboratory
- Genetic Testing
- Biobank
- Life Sciences
- Health
- Sequencing
website: https://galatea.bio/
---
