---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 43.7
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 55
  human_in_the_loop: 1
  name: Galatea Bio Agentic Access
  operation_count: 99
  slug: galatea-bio-agentic-access
  summary_line: 99 operations · 55 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: REST API (Swagger 2.0, 99 operations across 79 paths) for the Galatea Bio Octopod platform. Covers JWT authentication, source-file upload/validation, execution orders against named analysis models, ta
  name: Octopod Ancestry API
  slug: octopod-ancestry-api
artifact_total: 7
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
overview: 'Galatea Bio publishes 1 API on the [APIs.io](https://apis.io/) network: Octopod Ancestry API. Tagged areas include Genomics, Bioinformatics, Ancestry, Precision Medicine, and polygenic-risk-score.


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
  composite: 36.9
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 30.3
    contract_quality: 58.6
    developer_ergonomics: 35.1
    discoverability: 75.9
    governance: 30.3
    operational_transparency: 10.5
  previous_composite: 36.9
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
  schema_version: 0.12.1
  scored_at: '2026-08-24'
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
