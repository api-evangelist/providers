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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 4
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/validus-capital-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/validus-capital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://validusgrp.com/
- group: company
  title: ''
  type: Blog
  url: https://validusgrp.com/news-insights/
- group: company
  title: ''
  type: BlogRSS
  url: https://validusgrp.com/feed/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://validusgrp.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://validusgrp.com/assets/privacy-policy.pdf
- group: agent
  title: ''
  type: WellKnown
  url: well-known/validus-capital-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/validus-capital-security.txt
- group: auth
  title: ''
  type: Security
  url: security/validus-capital-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/validus-capital-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/validus-capital-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/validus-capital-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/validus-capital-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/validus-capital-rate-limits.yml
coverage:
  checked: '2026-09-02'
  detail: 'Validus ships SME lending only as an end-user product: the four-page group site at validusgrp.com has no developer section, no developer.* or docs.* subdomain resolves on any Validus domain, /openapi.json and /swagger.json 404 on every group and country host, and the one live API host, api.batumbu.id, answers every path with a plain-text "404 page not found" (the Singapore entity, Validus Capital Pte Ltd, was also sold to GXS Bank in April 2025 and validus.sg now redirects to the group site).'
  evidence:
  - status: 404
    url: https://validusgrp.com/openapi.json
  - status: 404
    url: https://validusgrp.com/developers/
  - status: 404
    url: https://api.batumbu.id/openapi.json
  - status: 404
    url: https://batumbu.id/.well-known/api-catalog
  - status: 200
    url: https://validus.sg/
  - status: 200
    url: https://validusgrp.com/.well-known/security.txt
  reason: no-developer-program
  state: none
created: '2026-09-02'
description: Validus is a Southeast Asian SME supply-chain and working-capital financing platform operated by Validus Investment Holdings Pte Ltd (UEN 201803167H), headquartered at Asia Square Tower 2 in Singapore and founded in 2015 to address the unmet financing needs of small and medium enterprises. The group runs country businesses across four markets — Batumbu (PT Berdayakan Usaha Indonesia) in Indonesia, Siam Validus in Thailand, Validus Vietnam, and, until April 2025, Validus Capital Pte Ltd in Singapore — offering invoice financing, purchase-order financing, vendor/supply-chain financing programs, working capital loans, SME business accounts and corporate cards funded by accredited and institutional investors. Validus Capital Pte Ltd, the Singapore subsidiary and the entity this profile is named for, was acquired outright by GXS Bank on 15 April 2025 and now trades as GXS Capital; the validus.sg domain redirects to the group site. The group has disbursed more than US$5 billion across
  its markets and has raised capital from Vertex Ventures, FMO, Citi, HSBC, Oikocredit and K3 Ventures. Validus publishes no public developer program, API reference or machine-readable API contract on any of its group or country domains.
image: https://validusgrp.com/wp-content/uploads/2025/01/Logo-Red.png
layout: provider
modified: '2026-09-02'
name: Validus Capital
nav: Providers
network: true
overview: 'Validus Capital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Financial Services, Lending, SME Finance, and Fintech.


  Validus Capital''s developer surface includes engineering blog and 14 more developer resources.'
plans:
- name: Validus Capital Plans Pricing
  plan_count: 0
  slug: validus-capital-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Validus Capital Rate Limits
  slug: validus-capital-rate-limits
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 12.6
  provenance:
    conformance: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Validus Capital Domain Security
  slug: validus-capital-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Validus Capital Vulnerability Disclosure
  slug: validus-capital-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: validus-capital
tags:
- Company
- Financial Services
- Lending
- SME Finance
- Fintech
- Supply Chain Finance
- Invoice Financing
- Working Capital
- Southeast Asia
- Singapore
website: https://validusgrp.com/
---
