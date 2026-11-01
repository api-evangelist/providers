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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Compliance
  url: https://docuten.com/en/security-policy/
- group: other
  href: https://artifacts.apis.io/docuten/hosts/docuten-hosts.yml
  title: ''
  type: Hosts
  url: hosts/docuten-hosts.yml
- group: other
  href: https://artifacts.apis.io/docuten/vendors/docuten-vendors.yml
  title: ''
  type: Vendors
  url: vendors/docuten-vendors.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developers.docuten.com/es/
- group: auth
  href: https://artifacts.apis.io/docuten/security/docuten-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/docuten-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/docuten/security/docuten-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/docuten-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docuten.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docuten.com/es/apis-e-integracion/documentacion-de-apis/
- group: company
  title: ''
  type: Blog
  url: https://docuten.com/es/blog/
- group: operate
  title: ''
  type: Support
  url: https://docuten.com/es/contacto/
created: '2026-10-20'
description: Docuten provides digital compliance solutions for electronic invoicing, document signing, and regulatory filing across multiple sectors such as food, logistics, construction, and education. Their platform enables businesses to automate electronic invoices, receive invoices, digitally sign internal and commercial documents, and manage transport documentation like DeCA and eCMR, ensuring legal validity and streamlined processes. Docuten also offers integrations with ERP systems and APIs for developers to embed these capabilities into their own applications.
image: https://docuten.com/wp-content/uploads/2026/07/oficina-docuten.jpg
layout: provider
modified: '2026-10-20'
name: Docuten
nav: Providers
network: true
overview: 'Docuten is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include API, Invoicing, Document Signing, Compliance, and Spain.


  Docuten''s developer surface includes API reference, documentation, engineering blog, support, and 6 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 12.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Docuten Domain Security
  slug: docuten-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Docuten Trust Center
  slug: docuten-trust-center
  summary_line: ISO 27001, GDPR
slug: docuten
tags:
- API
- Invoicing
- Document Signing
- Compliance
- Spain
website: https://docuten.com/
---
