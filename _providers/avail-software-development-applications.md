---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
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
  score: 15.1
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 3
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/llms/avail-software-development-applications-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/avail-software-development-applications-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/well-known/avail-software-development-applications-clarity-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/avail-software-development-applications-clarity-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/plans/avail-software-development-applications-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/avail-software-development-applications-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/changelog/avail-software-development-applications-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/avail-software-development-applications-changelog.yml
- group: auth
  title: ''
  type: Security
  url: https://clarity.com/vdp
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/well-known/avail-software-development-applications-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/avail-software-development-applications-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/hosts/avail-software-development-applications-hosts.yml
  title: ''
  type: Hosts
  url: hosts/avail-software-development-applications-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/vendors/avail-software-development-applications-vendors.yml
  title: ''
  type: Vendors
  url: vendors/avail-software-development-applications-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getavail.com/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://login.getavail.com/signin/register
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getavail.com/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://blog.getavail.com/tag/release-notes
- group: company
  title: ''
  type: Blog
  url: https://blog.getavail.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/security/avail-software-development-applications-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/avail-software-development-applications-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/avail-software-development-applications/refs/heads/main/security/avail-software-development-applications-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/avail-software-development-applications-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.availproject.org/
coverage:
  checked: 2026-09-26
  detail: The company website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://www.getavail.com
  reason: no-developer-program
  state: unreadable
created: '2026-09-26'
description: Avail offers a content management system for architecture, engineering, and construction (AEC) teams that use Revit, AutoCAD, and Civil 3D. The platform lets firms organize, search, and reuse technical content such as block libraries, drawings, and PDFs across multiple file types and storage services. It integrates with existing infrastructure like OneDrive, BIM360, and Egnyte, and provides visual navigation tools such as thumbnails and channel cards.
image: https://cdn.prod.website-files.com/69dfc405efb79040457a8ff2/6a85f2b2111a9d8b58e64733_OG-AVAIL%20standard.png
layout: provider
modified: '2026-09-26'
name: Avail Software Development Applications
nav: Providers
network: true
overview: 'Avail Software Development Applications is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Content Management, AEC, Revit, AutoCAD, and Civil 3D.


  Avail Software Development Applications'' developer surface includes changelog, signup flow, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Avail Software Development Applications Plans Pricing
  plan_count: 4
  slug: avail-software-development-applications-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 23.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 55.4
    operational_transparency: 26.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.6
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Avail Software Development Applications Domain Security
  slug: avail-software-development-applications-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Avail Software Development Applications Vulnerability Disclosure
  slug: avail-software-development-applications-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: avail-software-development-applications
tags:
- Content Management
- AEC
- Revit
- AutoCAD
- Civil 3D
- BIM
website: https://www.availproject.org/
---
