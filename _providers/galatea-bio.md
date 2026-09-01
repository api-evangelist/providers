---
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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 55
  human_in_the_loop: 1
  name: Galatea Bio Agentic Access
  operation_count: 99
  slug: galatea-bio-agentic-access
  summary_line: 99 operations · 55 acting · 1 human-in-the-loop
api_count: 2
apis:
- description: The auth API from Galatea Bio — 5 operation(s) for auth.
  name: Galatea Bio Auth API
  slug: galatea-bio-auth-api
- description: The credit API from Galatea Bio — 14 operation(s) for credit.
  name: Galatea Bio Credit API
  slug: galatea-bio-credit-api
- description: The dashboard API from Galatea Bio — 7 operation(s) for dashboard.
  name: Galatea Bio Dashboard API
  slug: galatea-bio-dashboard-api
- description: The data API from Galatea Bio — 12 operation(s) for data.
  name: Galatea Bio Data API
  slug: galatea-bio-data-api
- description: The exec API from Galatea Bio — 11 operation(s) for exec.
  name: Galatea Bio Exec API
  slug: galatea-bio-exec-api
- description: The internal API from Galatea Bio — 4 operation(s) for internal.
  name: Galatea Bio Internal API
  slug: galatea-bio-internal-api
- description: The notification API from Galatea Bio — 3 operation(s) for notification.
  name: Galatea Bio Notification API
  slug: galatea-bio-notification-api
- description: The organizations API from Galatea Bio — 13 operation(s) for organizations.
  name: Galatea Bio Organizations API
  slug: galatea-bio-organizations-api
- description: The statistics API from Galatea Bio — 2 operation(s) for statistics.
  name: Galatea Bio Statistics API
  slug: galatea-bio-statistics-api
- description: The users API from Galatea Bio — 8 operation(s) for users.
  name: Galatea Bio Users API
  slug: galatea-bio-users-api
artifact_total: 16
asyncapis:
- description: ''
  name: Galatea Bio Octopod Webhooks
  slug: galatea-bio-octopod-webhooks
common:
- group: agent
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
  title: ''
  type: Authentication
  url: authentication/galatea-bio-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/galatea-bio-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/galatea-bio-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/galatea-bio-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/galatea-bio-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/galatea-bio-conformance.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/galatea-bio-octopod-webhooks.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/galatea-bio-sandbox.yml
- group: build
  title: ''
  type: Packages
  url: packages/galatea-bio-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/galatea-bio-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/galatea-bio-cli.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/galatea-bio-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/galatea-bio-octopod-overlay.yaml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/galatea-bio-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/galatea-bio-plans-pricing.yml
- group: auth
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
overview: 'Galatea Bio publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Auth API, Credit API, Dashboard API, and 7 more. Tagged areas include Genomics, Bioinformatics, Ancestry, Precision Medicine, and polygenic-risk-score.


  The Galatea Bio catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Galatea Bio''s developer surface includes documentation, API reference, getting-started guide, authentication, sandbox, CLI, and 20 more developer resources.'
plans:
- name: Galatea Bio Plans Pricing
  plan_count: 0
  slug: galatea-bio-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: Galatea Bio Rate Limits
  slug: galatea-bio-rate-limits
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 21
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 18.2
    contract_quality: 56.2
    developer_ergonomics: 35.1
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 34.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 27.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/galatea-bio/refs/heads/main/screenshots/galatea-bio-2026-08-17T080949.png
security:
- kind: authentication
  name: Galatea Bio Authentication
  slug: galatea-bio-authentication
  summary_line: apiKey/http-bearer · 1 scheme
- kind: domain-security
  name: Galatea Bio Domain Security
  slug: galatea-bio-domain-security
  summary_line: TLSv1.3 · DMARC
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
