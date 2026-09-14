---
access_model:
  confidence: high
  label: No published plans — access by agreement
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  - https://health.mil/Military-Health-Topics/Technology/Support-Areas/MDR-M2-ICD-Functional-References-and-Specification-Documents
  trial: false
  try_now: false
api_count: 1
apis:
- description: 'MHS Genesis, the Department of Defense electronic health record built on Oracle Health (Cerner), exposes a SMART on FHIR interface for authorized clinical applications to read and write patient data. '
  name: MHS Genesis SMART on FHIR API
  slug: mhs-genesis-smart-on-fhir
artifact_total: 6
collections:
- collection_type: open
  name: API Collection
  slug: open-defense-health-agency
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/defense-health-agency-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/defense-health-agency
- group: company
  title: ''
  type: Website
  url: https://www.health.mil
- group: company
  title: ''
  type: About
  url: https://www.dha.mil/About-DHA
- group: other
  title: ''
  type: x-Publications
  url: https://www.health.mil/Reference-Center
- group: company
  title: ''
  type: Newsroom
  url: https://www.health.mil/News
- group: design
  title: ''
  type: Conformance
  url: conformance/defense-health-agency-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/defense-health-agency-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/defense-health-agency-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/defense-health-agency-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.health.mil/News/Articles
- group: company
  title: ''
  type: BlogRSS
  url: https://health.mil/RSS/Articles
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dpcld.defense.gov/Privacy.aspx
- group: other
  title: ''
  type: x-InterfaceControlDocuments
  url: https://health.mil/Military-Health-Topics/Technology/Support-Areas/MDR-M2-ICD-Functional-References-and-Specification-Documents/Interface-Control-Documents-Functional-References-and-Specifications
- group: other
  title: ''
  type: x-TechnologyPrograms
  url: https://www.health.mil/Military-Health-Topics/Technology
coverage:
  checked: '2026-09-07'
  detail: DHA's only published interface reference is a set of 32 Interface Control Documents for MHS Data Repository feeds, served as .DOCX and .PDF from the Health.mil Reference Center, with no OpenAPI, FHIR CapabilityStatement, WSDL or .proto anywhere on health.mil, dha.mil or tricare.mil, and the developer request path behind them (info.health.mil) is served under a DoD-internal PKI certificate that no public client can complete a TLS handshake with.
  evidence:
  - status: 200
    url: https://health.mil/Military-Health-Topics/Technology/Support-Areas/MDR-M2-ICD-Functional-References-and-Specification-Documents/Interface-Control-Documents-Functional-References-and-Specifications
  - status: 200
    url: https://www.health.mil/Reference-Center/Technical-Documents/2015/11/15/ICD-TED-I
  - status: 404
    url: https://www.health.mil/.well-known/api-catalog
  - status: 404
    url: https://www.health.mil/llms.txt
  - status: 0
    url: https://info.health.mil/apps/HIT/services/SitePages/escMenu.aspx
  reason: pdf-only-docs
  state: unreadable
created: '2024-12-03'
description: 'The Defense Health Agency (DHA) is a joint, integrated combat support agency that enables the Army, Navy, and Air Force medical services to provide a medically ready force and ready medical force to combatant commands. DHA operates the Military Health System (MHS), MHS Genesis electronic health record, the Military Health System Data Repository (MDR), and the Enterprise Intelligence and Data Solutions (EIDS) program. Data exchange inside MHS Genesis uses SMART on FHIR APIs, but DHA does not currently publish a general-purpose public developer API, a developer portal, or any machine-readable API contract. What it does publish is human-readable interface documentation: 32 Interface Control Documents for MHS Data Repository feeds, plus MDR and M2 data dictionaries and access guides, all distributed as .DOCX and .PDF through the Health.mil Reference Center.'
finops:
- name: Defense Health Agency Finops
  service_category: API
  slug: defense-health-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/defense-health-agency.png
layout: provider
modified: '2026-09-07'
name: Defense Health Agency
nav: Providers
network: true
overview: 'Defense Health Agency publishes 1 API on the [APIs.io](https://apis.io/) network: MHS Genesis SMART on FHIR API. Tagged areas include Federal-Government, Defense, Department of Defense, Health, and Military Health System.


  Defense Health Agency''s developer surface includes engineering blog and 14 more developer resources.'
plans:
- name: Defense Health Agency Plans Pricing
  plan_count: 0
  slug: defense-health-agency-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Defense Health Agency Rate Limits
  slug: defense-health-agency-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/defense-health-agency/refs/heads/main/screenshots/defense-health-agency-2026-06-20T175826.png
security:
- kind: domain-security
  name: Defense Health Agency Domain Security
  slug: defense-health-agency-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: defense-health-agency
tags:
- Federal-Government
- Defense
- Department of Defense
- Health
- Military Health System
- MHS Genesis
- FHIR
- Health IT
website: https://www.health.mil
---
