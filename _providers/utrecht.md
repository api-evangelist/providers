---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 121
  human_in_the_loop: 4
  name: Utrecht Agentic Access
  operation_count: 121
  slug: utrecht-agentic-access
  summary_line: 121 operations · 121 acting · 4 human-in-the-loop
api_count: 21
apis:
- description: 'OAI-PMH metadata harvesting interface for the Utrecht University Library DSpace institutional repository, exposing publication and resource metadata of Utrecht University and UMC Utrecht researchers. '
  name: Utrecht University Repository OAI-PMH
  slug: repository-oai
- description: The admin API from Utrecht University — 1 operation(s) for admin.
  name: Utrecht University admin API
  slug: utrecht-admin-api
- description: The browse API from Utrecht University — 4 operation(s) for browse.
  name: Utrecht University browse API
  slug: utrecht-browse-api
- description: The data_access_token API from Utrecht University — 4 operation(s) for data_access_token.
  name: Utrecht University data_access_token API
  slug: utrecht-data-access-token-api
- description: The datarequest API from Utrecht University — 34 operation(s) for datarequest.
  name: Utrecht University datarequest API
  slug: utrecht-datarequest-api
- description: The folder API from Utrecht University — 7 operation(s) for folder.
  name: Utrecht University folder API
  slug: utrecht-folder-api
- description: The groups API from Utrecht University — 15 operation(s) for groups.
  name: Utrecht University groups API
  slug: utrecht-groups-api
- description: The meta API from Utrecht University — 2 operation(s) for meta.
  name: Utrecht University meta API
  slug: utrecht-meta-api
- description: The meta_form API from Utrecht University — 2 operation(s) for meta_form.
  name: Utrecht University meta_form API
  slug: utrecht-meta-form-api
- description: The notifications API from Utrecht University — 3 operation(s) for notifications.
  name: Utrecht University notifications API
  slug: utrecht-notifications-api
- description: The provenance API from Utrecht University — 1 operation(s) for provenance.
  name: Utrecht University provenance API
  slug: utrecht-provenance-api
- description: The publication_troubleshoot API from Utrecht University — 1 operation(s) for publication_troubleshoot.
  name: Utrecht University publication_troubleshoot API
  slug: utrecht-publication-troubleshoot-api
- description: The research API from Utrecht University — 13 operation(s) for research.
  name: Utrecht University research API
  slug: utrecht-research-api
- description: The revisions API from Utrecht University — 3 operation(s) for revisions.
  name: Utrecht University revisions API
  slug: utrecht-revisions-api
- description: The schema API from Utrecht University — 1 operation(s) for schema.
  name: Utrecht University schema API
  slug: utrecht-schema-api
- description: The schema_transformation API from Utrecht University — 1 operation(s) for schema_transformation.
  name: Utrecht University schema_transformation API
  slug: utrecht-schema-transformation-api
- description: The settings API from Utrecht University — 2 operation(s) for settings.
  name: Utrecht University settings API
  slug: utrecht-settings-api
- description: The stats API from Utrecht University — 4 operation(s) for stats.
  name: Utrecht University stats API
  slug: utrecht-stats-api
- description: The vault API from Utrecht University — 16 operation(s) for vault.
  name: Utrecht University vault API
  slug: utrecht-vault-api
- description: The vault_archive API from Utrecht University — 3 operation(s) for vault_archive.
  name: Utrecht University vault_archive API
  slug: utrecht-vault-archive-api
- description: The vault_deaccession API from Utrecht University — 4 operation(s) for vault_deaccession.
  name: Utrecht University vault_deaccession API
  slug: utrecht-vault-deaccession-api
artifact_total: 37
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/utrecht-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/utrecht-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/utrecht-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/utrecht-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.uu.nl/en
- group: build
  title: ''
  type: GitHub
  url: https://github.com/UtrechtUniversity
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/utrecht-university/
- group: other
  title: ''
  type: Repository
  url: https://dspace.library.uu.nl/
- group: commercial
  title: ''
  type: Plans
  url: plans/utrecht-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/utrecht-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/utrecht-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Utrecht University (Universiteit Utrecht) is a public research university in Utrecht, Netherlands, ranked #105 in the QS World University Rankings 2025. Its public developer and API footprint is centered on open research infrastructure rather than a formal developer portal: the Utrecht University Library runs a DSpace institutional repository exposing publication metadata via OAI-PMH, the university maintains a large public GitHub organization (UtrechtUniversity) that publishes open-source research software, and it develops Yoda, an iRODS-based research data management platform. There is no single consolidated, self-service API developer portal; most administrative and identity systems are gated behind institutional SolisID/SSO.'
examples:
- key_count: 4
  name: Utrecht Yoda Datarequest Submit Example
  slug: utrecht-yoda-datarequest-submit-example
- key_count: 5
  name: Utrecht Yoda Folder Submit Example
  slug: utrecht-yoda-folder-submit-example
finops:
- name: Utrecht Finops
  service_category: Education
  slug: utrecht-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/utrecht.png
json_schemas:
- name: Yoda API Error Result
  property_count: 3
  slug: utrecht-yoda-error
- name: Yoda API Result
  property_count: 3
  slug: utrecht-yoda-result
json_structures:
- name: Utrecht Yoda Error Structure
  property_count: 3
  slug: utrecht-yoda-error-structure
- name: Utrecht Yoda Result Structure
  property_count: 3
  slug: utrecht-yoda-result-structure
jsonld:
- class_count: 19
  name: Utrecht Context
  property_count: 3
  slug: utrecht-context
layout: provider
modified: '2026-06-03'
name: Utrecht University
nav: Providers
network: true
overview: 'Utrecht University publishes 20 APIs on the [APIs.io](https://apis.io/) network, including admin API, browse API, data_access_token API, and 17 more. Tagged areas include Education, Higher Education, University, Netherlands, and Research Data.


  The Utrecht University catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Utrecht University''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: Utrecht Plans Pricing
  plan_count: 2
  slug: utrecht-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 1
  name: Utrecht Rate Limits
  slug: utrecht-rate-limits
rules:
- name: Utrecht University API Rules
  rule_count: 4
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 3
  slug: utrecht-jsonschema-spectral-rules
- name: Utrecht University API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: utrecht-rules
score:
  band: thin
  composite: 41.7
  delta: -4.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 63.6
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 45.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/utrecht/refs/heads/main/screenshots/utrecht-2026-06-20T200730.png
security:
- kind: authentication
  name: Utrecht Authentication
  slug: utrecht-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Utrecht Domain Security
  slug: utrecht-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Utrecht Vulnerability Disclosure
  slug: utrecht-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: utrecht
tags:
- Education
- Higher Education
- University
- Netherlands
- Research Data
- Open Access
- Library
- Open Source
website: https://www.uu.nl/en
---
