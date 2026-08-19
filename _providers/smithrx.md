---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/smithrx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smithrx.com/
- group: company
  title: ''
  type: Blog
  url: https://smithrx.com/blog
- group: operate
  title: ''
  type: Support
  url: https://smithrx.com/contact
- group: operate
  title: ''
  type: FAQ
  url: https://smithrx.com/faqs
- group: commercial
  title: ''
  type: TermsOfService
  url: https://smithrx.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://smithrx.com/privacy-policy
- group: start
  title: ''
  type: Login
  url: https://member.mysmithrx.com/login
- group: start
  title: ''
  type: MemberPortal
  url: https://smithrx.com/portal
- group: start
  title: ''
  type: PartnerPortal
  url: https://partner.mysmithrx.com/
- group: company
  title: ''
  type: Careers
  url: https://smithrx.com/careers
- group: company
  title: ''
  type: News
  url: https://smithrx.com/news
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/smithrx_stock/
- group: auth
  title: ''
  type: Security
  url: https://smithrx.com/security
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/smithrx-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.smithrx.com/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.smithrx.com/
- group: other
  title: ''
  type: Accreditation
  url: https://accreditnet.urac.org/directory/#/accreditation/PBM010015/info
- group: design
  title: ''
  type: Conformance
  url: conformance/smithrx-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/smithrx-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/smithrx-llms.txt
created: '2026-08-02'
description: SmithRx (legal entity Smith Health, Inc.) is a pass-through pharmacy benefit manager (PBM) for self-insured employers, founded by Jake Frenz. It operates its own in-house claims adjudication platform and a "Drug Pathways Engine" that routes every pharmacy claim to the lowest net cost pathway across drug selection, source and pricing. SmithRx sells through brokers, TPAs and benefits consultants, serves members through a member portal, and serves brokers and TPAs through a partner portal. It is URAC-accredited for Pharmacy Benefit Management. SmithRx publishes no public developer portal, API documentation or machine-readable API contract; its platform marketing describes "secure APIs" used to connect a customer plan to existing vendors, but that surface is private and partner-gated.
image: https://framerusercontent.com/images/WlIGH06EWF670OjheE0Qs5kYuxE.jpg
layout: provider
modified: '2026-08-02'
name: SmithRx
nav: Providers
network: true
overview: 'SmithRx is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Care, Pharmacy, Pharmacy Benefit Management, and Prescription Drugs.


  SmithRx''s developer surface includes engineering blog, support, FAQ, product news, and 17 more developer resources.'
random_paper: 38
score:
  band: emerging
  composite: 22.1
  delta: -1.6
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 10.5
  previous_composite: 23.7
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 45.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Smithrx Domain Security
  slug: smithrx-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Smithrx Vulnerability Disclosure
  slug: smithrx-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Smithrx Trust Center
  slug: smithrx-trust-center
  summary_line: SOC 2, HIPAA
slug: smithrx
tags:
- Company
- Health Care
- Pharmacy
- Pharmacy Benefit Management
- Prescription Drugs
- Employee Benefits
- Claims
- Insurance
- Health Technology
website: https://smithrx.com/
---
