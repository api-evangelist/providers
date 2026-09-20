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
  scored_at: '2026-09-19'
api_count: 0
artifact_total: 2
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affineon-health/refs/heads/main/security/affineon-health-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/affineon-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.affineon.com/
- group: company
  title: ''
  type: About
  url: https://www.affineon.com/company
- group: company
  title: ''
  type: Blog
  url: https://www.affineon.com/news
- group: operate
  title: ''
  type: Contact
  url: https://www.affineon.com/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.affineon.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.affineon.com/labs-core
- group: operate
  title: ''
  type: Support
  url: https://resources.affineon.com/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://inboxmanagement.affineon.com/
- group: company
  title: ''
  type: Partners
  url: https://marketplace.athenahealth.com/product/affineon-health
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/affineon/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/affineon
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/affineon-health/refs/heads/main/llms/affineon-health-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/affineon-health-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/affineon-health/refs/heads/main/plans/affineon-health-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/affineon-health-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/affineon-health/refs/heads/main/conformance/affineon-health-conformance.yml
  title: ''
  type: Conformance
  url: conformance/affineon-health-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/affineon-health/refs/heads/main/conformance/affineon-health-conformance.yml
  title: ''
  type: Compliance
  url: conformance/affineon-health-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/affineon-health/refs/heads/main/packages/affineon-health-packages.yml
  title: ''
  type: Packages
  url: packages/affineon-health-packages.yml
coverage:
  checked: '2026-09-12'
  detail: Affineon markets "Affineon Embed", a white-label program for EHRs and AI scribes that promises "minimal integration", but publishes no developer host at all — api.affineon.com, docs.affineon.com, developers.affineon.com and app.affineon.com do not resolve in DNS, certificate transparency for *.affineon.com lists only cpanel/mail/webmail/webdisk/www/resources/inboxmanagement, and the only route to the integration is the "Request Access" contact form on /embed.
  evidence:
  - status: 200
    url: https://www.affineon.com/embed
  - status: 404
    url: https://www.affineon.com/openapi.json
  - status: 404
    url: https://www.affineon.com/.well-known/api-catalog
  - status: 200
    url: https://www.affineon.com/llms.txt
  - status: 200
    url: https://marketplace.athenahealth.com/product/affineon-health
  reason: sales-gate
  state: gated
created: '2026-09-12'
description: 'Affineon Health is a healthcare AI company whose product is an AI inbox agent that works inside a clinician''s existing EHR inbox rather than as a separate application. Two modules ship today: Labs Core, which routes CC''d results away from the provider, groups incomplete lab sets until they are ready, auto-processes normal and clinically insignificant results, trends and summarizes the chart, and drafts the patient message; and Rx Renewals, which clears prescription renewal requests that meet a practice protocol and escalates the rest for physician review. A third offering, Affineon Embed, is a white-label program letting EHR vendors, AI scribes and other health-technology companies bundle the same inbox agent into their own products — Commure is a named participant. Affineon reaches practices chiefly through the athenahealth Marketplace, states it is SOC 2 and HIPAA compliant, and publishes per-provider subscription pricing. It publishes no developer portal, API reference,
  SDK or machine-readable specification of any kind: the company is a consumer of EHR APIs, and its own integration surface is quoted through a Request Access form.'
image: https://cdn.prod.website-files.com/66608f8e74b455a259a339c6/671d8a08ecfa2180636b25f0_Affineon%20open%20graph%20image.png
layout: provider
modified: '2026-09-12'
name: Affineon Health
nav: Providers
network: true
overview: 'Affineon Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Artificial Intelligence, Clinical Workflow, and Electronic Health Records.


  Affineon Health''s developer surface includes engineering blog, pricing, support, and 14 more developer resources.'
plans:
- name: Affineon Health Plans Pricing
  plan_count: 5
  slug: affineon-health-plans-pricing
random_paper: 17
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 60.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 2.6
  previous_composite: 23.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 32.5
  schema_version: 0.22.0
  scored_at: '2026-09-19'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Affineon Health Domain Security
  slug: affineon-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: affineon-health
tags:
- Company
- Healthcare
- Artificial Intelligence
- Clinical Workflow
- Electronic Health Records
- Health IT
- Laboratory
- Prescriptions
- Care Coordination
- Physician Burnout
website: https://www.affineon.com/
---
