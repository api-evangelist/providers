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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: API documentation is provided at the Form Bio developer docs site.
  name: Form Bio API
  slug: form-bio-api-2
- baseURL: https://cli.formbio.com
  baseurl_source: declared
  description: The Form Bio API API from Form Bio — 1 operation(s) for form bio api.
  name: Form Bio Form Bio API
  slug: form-bio-form-bio-api-api
- baseURL: https://cli.formbio.com
  baseurl_source: declared
  description: The Public API from Form Bio — 1 operation(s) for public.
  name: Form Bio Public API
  slug: form-bio-public-api
artifact_total: 6
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/form-bio/refs/heads/main/rules/form-bio-rules.yml
  title: ''
  type: Spectral
  url: rules/form-bio-rules.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/form-bio/refs/heads/main/cli/form-bio-cli.yml
  title: ''
  type: CLI
  url: cli/form-bio-cli.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.formbio.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/form-bio/refs/heads/main/conformance/form-bio-conformance.yml
  title: ''
  type: Conformance
  url: conformance/form-bio-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/form-bio/refs/heads/main/hosts/form-bio-hosts.yml
  title: ''
  type: Hosts
  url: hosts/form-bio-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/form-bio/refs/heads/main/vendors/form-bio-vendors.yml
  title: ''
  type: Vendors
  url: vendors/form-bio-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.formbio.com/news
- group: docs
  title: ''
  type: Documentation
  url: https://docs.formbio.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.form.bio/creating-new-projects
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/formbio
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/form-bio/refs/heads/main/security/form-bio-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/form-bio-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/form-bio/refs/heads/main/security/form-bio-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/form-bio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.formbio.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.formbio.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.formbio.com/terms-of-use
coverage:
  checked: '2026-10-13'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.formbio.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-12'
description: Form Bio is an AI‑driven biotech company focused on accelerating the development of genetic medicines and genome engineering solutions. Leveraging proprietary AI platforms, Form Bio provides end‑to‑end services from vector design and optimization to manufacturing analytics, helping partners de‑risk and accelerate therapeutic programs across human and animal health.
image: https://cdn.prod.website-files.com/68f288490cb3cdefe2f4a51f/69039e70a649d722ba8c909c_homepage-og.jpg
layout: provider
modified: '2026-10-12'
name: Form Bio
nav: Providers
network: true
overview: 'Form Bio is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Form Bio API, Public API, and 1 more. Tagged areas include Company, Biotechnology, Artificial Intelligence, Genetic Medicine, and Genome Engineering.


  The Form Bio catalog on APIs.io includes 1 Spectral governance ruleset.


  Form Bio''s developer surface includes CLI, documentation, and 13 more developer resources.'
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: Form Bio API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: form-bio-rules
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.5
    catalog_earned_first_party: 0.0
    catalog_gap: 60.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 10.7
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
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
  name: Form Bio Domain Security
  slug: form-bio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Form Bio Trust Center
  slug: form-bio-trust-center
  summary_line: SOC 2, ISO 27001
slug: form-bio
tags:
- Company
- Biotechnology
- Artificial Intelligence
- Genetic Medicine
- Genome Engineering
website: https://www.formbio.com
---
