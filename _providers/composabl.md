---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: Composabl, now operating as AMESA, provides an advanced modular enterprise system for autonomous agent orchestration.
  name: AMESA Platform API
  slug: amesa-platform-api
- description: The Reference API from Composabl — 4 operation(s) for reference.
  name: Composabl Reference API
  slug: composabl-reference-api
artifact_total: 4
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/rules/composabl-rules.yml
  title: ''
  type: Spectral
  url: rules/composabl-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/cli/composabl-cli.yml
  title: ''
  type: CLI
  url: cli/composabl-cli.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/changelog/composabl-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/composabl-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/conformance/composabl-conformance.yml
  title: ''
  type: Conformance
  url: conformance/composabl-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/llms/composabl-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/composabl-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/well-known/composabl-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/composabl-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/hosts/composabl-hosts.yml
  title: ''
  type: Hosts
  url: hosts/composabl-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/vendors/composabl-vendors.yml
  title: ''
  type: Vendors
  url: vendors/composabl-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.amesa.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.amesa.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.amesa.com/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://docs.amesa.com/reference/glossary
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.amesa.com/getting-started
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/composabl/refs/heads/main/security/composabl-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/composabl-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.amesa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.amesa.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.amesa.com/
coverage:
  checked: '2026-10-10'
  detail: Documentation pages exist but no OpenAPI, GraphQL, AsyncAPI, gRPC, or WSDL files were found.
  evidence:
  - status: 200
    url: https://docs.amesa.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-09'
description: Composabl, now operating as AMESA, provides an advanced modular enterprise system for autonomous agent orchestration. The platform enables enterprises to design, train, and deploy intelligent agents at scale, offering tools for simulation, skill generation, and multi‑agent system management. AMESA focuses on industrial AI, delivering secure, data‑driven solutions for complex enterprise workflows.
image: https://framerusercontent.com/images/HgrehJaMFETtADKu2s9c5KbfxQ.png
layout: provider
modified: '2026-10-09'
name: Composabl
nav: Providers
network: true
overview: 'Composabl is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Reference API, and 1 more. Tagged areas include Artificial Intelligence, Enterprise, Automation, Agents, and Platform.


  The Composabl catalog on APIs.io includes 1 Spectral governance ruleset.


  Composabl''s developer surface includes CLI, changelog, API reference, getting-started guide, documentation, and 12 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 49
  extends:
  - spectral:oas
  name: Composabl API Rules
  rule_count: 8
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 1
  slug: composabl-rules
score:
  band: thin
  composite: 38.8
  coverage:
    artifact_dirs: 11
    catalog_earned: 36.5
    catalog_earned_first_party: 0.0
    catalog_gap: 63.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 78.6
    contract_governance: 18.2
    contract_quality: 9.4
    developer_ergonomics: 45.2
    discoverability: 64.3
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Composabl Domain Security
  slug: composabl-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: composabl
tags:
- Artificial Intelligence
- Enterprise
- Automation
- Agents
- Platform
- Company
website: https://www.amesa.com/
---
