---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: DocuWare provides a REST API documented at the developer portal.
  name: DocuWare REST API
  slug: docuware-rest-api
artifact_total: 4
common:
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/changelog/docuware-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/docuware-changelog.yml
- group: auth
  title: ''
  type: Compliance
  url: https://start.docuware.com/security
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/conformance/docuware-conformance.yml
  title: ''
  type: Conformance
  url: conformance/docuware-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/llms/docuware-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/docuware-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/well-known/docuware-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docuware-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/well-known/docuware-security-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docuware-security-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/well-known/docuware-api-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/docuware-api-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/well-known/docuware-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/docuware-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/hosts/docuware-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docuware-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/vendors/docuware-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docuware-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://start.docuware.com/de/toshiba-tec-germany-imaging-systems-gmbh-docuware-partner-case-study
- group: operate
  title: ''
  type: Support
  url: https://support.docuware.com/en-US%2F
- group: auth
  title: ''
  type: Security
  url: https://start.docuware.com/security
- group: company
  title: ''
  type: Blog
  url: https://start.docuware.com/blog/document-management
- group: start
  title: ''
  type: GettingStarted
  url: https://start.docuware.com/de/blog/produkt/onboarding-f%C3%BCr-intelligent-indexing-3-tipps-f%C3%BCr-den-erfolgreichen-start
- group: docs
  title: ''
  type: Documentation
  url: https://developer.docuware.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/security/docuware-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/docuware-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/security/docuware-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/docuware-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/docuware/refs/heads/main/security/docuware-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docuware-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://start.docuware.com
coverage:
  checked: '2026-10-15'
  detail: Developer portal provides HTML documentation but no machine‑readable OpenAPI/AsyncAPI/GraphQL spec was found.
  evidence:
  - status: 200
    url: https://developer.docuware.com/rest/index.html
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-14'
description: DocuWare provides cloud‑based document management and workflow automation solutions for businesses of all sizes. Its platform enables secure capture, storage, indexing, and retrieval of documents, along with advanced features like intelligent document processing, electronic signatures, and integration with popular enterprise applications. DocuWare helps organizations streamline processes, improve compliance, and enhance productivity through a scalable, SaaS‑delivered service.
layout: provider
modified: '2026-10-14'
name: DocuWare
nav: Providers
network: true
overview: 'DocuWare is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Document Management, Workflow Automation, Intelligent Document Processing, Cloud, and Enterprise Content Management.


  DocuWare''s developer surface includes changelog, support, engineering blog, getting-started guide, documentation, and 15 more developer resources.'
random_paper: 0
score:
  band: emerging
  composite: 24.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 60.7
    operational_transparency: 26.3
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docuware Domain Security
  slug: docuware-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Docuware Vulnerability Disclosure
  slug: docuware-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Docuware Trust Center
  slug: docuware-trust-center
  summary_line: HIPAA, GDPR
slug: docuware
tags:
- Document Management
- Workflow Automation
- Intelligent Document Processing
- Cloud
- Enterprise Content Management
- Invoice Processing
- Secure Archiving
website: https://start.docuware.com
---
