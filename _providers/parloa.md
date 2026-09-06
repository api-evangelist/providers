---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
  trial: false
  try_now: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-05'
api_count: 2
apis:
- description: The Parloa Agent Management Platform (AMP) is the primary product surface for designing, testing, scaling, optimizing, and securing AI voice and chat agents for contact centers. AMP supports custom RE
  name: Parloa Agent Management Platform (AMP)
  slug: parloa-agent-management-platform
- description: 'Parloa AMP can be extended with custom services exposed over REST that the AI agent calls during a conversation to retrieve customer data from CRM systems, look up orders, verify identity, or trigger '
  name: Parloa Custom REST Services Integration
  slug: parloa-custom-rest-services
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/parloa-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/parloa-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.parloa.com/
- group: other
  title: ''
  type: Developer
  url: https://docs.amp.parloa.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.parloa.com/
- group: company
  title: ''
  type: Blog
  url: https://www.parloa.com/resources/blog/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.amp.parloa.com/getting-started/release-notes
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.parloa.com/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.parloa.com/terms-and-conditions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/parloa/
- group: operate
  title: ''
  type: Support
  url: https://www.parloa.com/contact/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.parloa.com/llms.txt
created: '2026-05-23'
description: Parloa is an enterprise conversational AI platform for contact centers that automates voice and chat customer interactions across industries including financial services, utilities, eCommerce, healthcare, media, and IT. The Parloa Agent Management Platform (AMP) supports designing, testing, scaling, optimizing, and securing AI agents that integrate with CCaaS, telephony, CRM, and ERP systems. Parloa is a sales-led enterprise product and developer access to its REST APIs and integration tooling is provided through customer and partner accounts rather than a fully public developer portal.
finops:
- name: Parloa Finops
  service_category: API
  slug: parloa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/parloa.png
layout: provider
modified: '2026-05-23'
name: Parloa
nav: Providers
network: true
overview: 'Parloa publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Agents, Artificial Intelligence, Call Center, CCaaS, and Contact Center.


  Parloa''s developer surface includes documentation, engineering blog, changelog, support, and 8 more developer resources.'
plans:
- name: Parloa Plans Pricing
  plan_count: 1
  slug: parloa-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Parloa Rate Limits
  slug: parloa-rate-limits
score:
  band: emerging
  composite: 19.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 51.0
    catalog_earned_first_party: 0.0
    catalog_gap: 64.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 19.2
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/parloa/refs/heads/main/screenshots/parloa-2026-06-20T191418.png
security:
- kind: domain-security
  name: Parloa Domain Security
  slug: parloa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Parloa Trust Center
  slug: parloa-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: parloa
tags:
- Agents
- Artificial Intelligence
- Call Center
- CCaaS
- Contact Center
- Conversational AI
- Customer Experience
- CX
- Generative AI
- Telephony
- Voice
website: https://www.parloa.com/
---
