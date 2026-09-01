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
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iag-domain-security.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/iag
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/iag-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/iag-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iag-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.iag.com.au/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/InsuranceAustraliaGroup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/iagcl
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iag
- group: company
  title: ''
  type: Newsroom
  url: https://www.iag.com.au/newsroom
- group: start
  title: ''
  type: SupplierPortal
  url: https://www.iag.com.au/supplier-portal
- group: start
  title: ''
  type: PartnerPortal
  url: https://www.cgu.com.au/eai/help
- group: operate
  title: ''
  type: Contact
  url: https://www.iag.com.au/contact-us
- group: other
  title: ''
  type: CorporateGovernance
  url: https://www.iag.com.au/about-us/corporate-governance/codes-and-policies
- group: company
  title: ''
  type: Careers
  url: https://careers.iag.com.au/
created: '2026-07-25'
description: 'Insurance Australia Group (IAG, ASX: IAG) is the largest general insurance company in Australia and New Zealand, headquartered in Sydney and operating a portfolio of underwriting brands rather than a single consumer-facing label. In Australia it trades as NRMA Insurance, CGU, WFI, Swann Insurance and the digital-native ROLLiN''; in New Zealand as State, AMI, NZI and Lumley. Its lines of business are property and casualty — home and contents, motor, commercial, rural and farm, compulsory third party and specialty — split across a Direct Insurance Australia arm and an Intermediated Insurance Australia arm that sells through brokers and authorised representatives. IAG has no public, self-serve API surface. Probing every conventional developer hostname on iag.com.au, cgu.com.au and nrma.com.au found no developer portal and no published reference documentation; docs.iag.com.au exists but immediately redirects to a Microsoft Entra ID sign-in and is an internal wall, not a portal.
  What the probes did confirm is a real Apigee API gateway fronting three brand virtual hosts — api.iag.com.au, api.cgu.com.au and api.nrma.com.au — each returning an Apigee ApplicationNotFound fault at the root, meaning proxies exist but none is discoverable or documented to the public. A second round of probing added a fourth brand virtual host, api.wfi.com.au, and a publicly resolvable non-production Apigee organisation at test-api.iag.com.au. IAG has also deployed MuleSoft''s Anypoint API Experience Hub and is migrating roughly 600 APIs onto it, with a stated intent to make them agent aware — a substantial API estate that is entirely internal. Broker and partner integration in this market runs through human-facing trading portals — CGU''s PolicyPlace quote-and-bind platform, the Ebix Sunrise Exchange and the Steadfast Client Trading Platform — not through an open API programme. IAG does run a HackerOne vulnerability disclosure programme, and published an RFC 9116 security.txt across
  seven brand domains until it was withdrawn in mid-2025. Australia has the legal machinery for open insurance and no live obligation: the Consumer Data Right that opened banking and energy was flagged for general insurance and then paused, so nothing compels IAG to publish. This record is therefore an honest stub: a partner-gated carrier with a private gateway and zero public specifications.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-25'
name: Insurance Australia Group
nav: Providers
network: true
overview: Insurance Australia Group is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Australia, New Zealand, Property and Casualty, and General Insurance.
random_paper: 11
score:
  band: minimal
  composite: 7.8
  coverage:
    artifact_dirs: 5
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 4.5
    operational_transparency: 13.2
  previous_composite: 7.8
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 25.8
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iag/refs/heads/main/screenshots/iag-2026-07-25T221946.png
security:
- kind: domain-security
  name: Iag Domain Security
  slug: iag-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Iag Vulnerability Disclosure
  slug: iag-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: iag
tags:
- Insurance
- Australia
- New Zealand
- Property and Casualty
- General Insurance
- Carrier
- Underwriting
- Claims
- Brokers
- Partner Gated
website: https://www.iag.com.au/
---
