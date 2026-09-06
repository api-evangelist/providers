---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
api_count: 1
apis:
- description: The CIOC publishes its charter, leadership roster, committee output, playbooks (e.g., Cloud Smart, Modular Contracting, IT Modernization), and federal IT guidance through cio.gov and councils.gov. The
  name: Chief Information Officers Council Resources
  slug: cioc-resources
artifact_total: 21
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chief-information-officers-council-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/chief-information-officers-council-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/chief-information-officers-council-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/chief-information-officers-council-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/chief-information-officers-council-finops.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/federal-cio-council
- group: company
  title: ''
  type: Website
  url: https://www.councils.gov/cioc
- group: company
  title: ''
  type: LegacyWebsite
  url: https://cio.gov
- group: other
  title: ''
  type: ParentAgency
  url: https://www.whitehouse.gov/omb/
- group: other
  title: ''
  type: Statute
  url: https://www.law.cornell.edu/uscode/text/44/3603
- group: other
  title: ''
  type: ExecutiveOrder
  url: https://www.federalregister.gov/documents/1996/07/19/96-18555/federal-information-technology
- group: other
  title: ''
  type: GSAOfficeOfGovernmentwidePolicy
  url: https://www.gsa.gov/policy-regulations/policy/information-technology-policy
- group: other
  title: ''
  type: FedRAMP
  url: https://www.fedramp.gov
- group: other
  title: ''
  type: TechnologyModernizationFund
  url: https://tmf.cio.gov
- group: other
  title: ''
  type: USAGov
  url: https://www.usa.gov/agencies/chief-information-officers-council
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.gsa.gov/website-information/website-policies
- group: other
  title: ''
  type: KnowledgeBase
  url: https://www.councils.gov/resources/?council=CIOC
- group: company
  title: ''
  type: Newsroom
  url: https://www.councils.gov/news-events/?council=CIOC
- group: other
  title: ''
  type: x-CouncilMembers
  url: https://www.councils.gov/cioc/members-leaders/
- group: other
  title: ''
  type: x-Charter
  url: https://www.councils.gov/docs/CIOC-Charter-Dec-2020.pdf
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/GSA/councils.gov
- group: other
  title: ''
  type: Committees
  url: ''
- group: other
  title: ''
  type: Programs
  url: ''
- group: other
  title: ''
  type: Standards
  url: ''
coverage:
  checked: '2026-09-05'
  detail: The CIO Council is a federal interagency policy forum, not a software publisher — its output is guidance, playbooks and a charter served as static Astro pages and PDFs on councils.gov, and a named-path probe of www.councils.gov, councils.gov and cio.gov on 2026-09-05 returned 404 (or a 301 to www) for every OpenAPI, GraphQL, MCP, agent-card, llms.txt and apis.json location, with a negative-control path confirming none of those hosts echoes paths.
  evidence:
  - status: 200
    url: https://www.councils.gov/cioc/
  - status: 404
    url: https://www.councils.gov/openapi.json
  - status: 404
    url: https://www.councils.gov/.well-known/agent-card.json
  - status: 404
    url: https://www.councils.gov/.well-known/apis.json
  - status: 301
    url: https://cio.gov/
  - status: 404
    url: https://cio.gov/openapi.json
  - status: 404
    url: https://www.councils.gov/.well-known/cioc-negative-control-7f3ab91c.json
  reason: not-a-software-company
  state: none
created: '2024-12-03'
description: The Chief Information Officers Council (CIOC) is the principal interagency forum for improving agency practices related to the design, acquisition, development, modernization, use, sharing, and performance of federal information resources. Established by Executive Order 13011 in 1996 and codified in the E-Government Act of 2002 (44 U.S.C. 3603), the Council is comprised of the Chief Information Officers and Deputy CIOs of executive branch agencies, the Federal CIO at OMB (who serves as Chair), the Federal Chief Information Security Officer, and the Administrator for Electronic Government. The CIOC develops recommendations for OMB IT policy, identifies opportunities to improve federal IT performance, coordinates multi-agency IT initiatives such as cybersecurity and cloud adoption, supports federal IT workforce development, and disseminates effective IT management practices across the federal government. The Council publishes guidance, playbooks, committee output and its charter
  through councils.gov, the consolidated federal executive councils hub GSA launched in March 2026; its long-standing home at cio.gov now redirects there. The Council operates no developer program and publishes no API.
features:
- name: Senior-Level Interagency Forum
- name: Federal IT Policy Coordination
- name: Cybersecurity Standards and Guidance
- name: IT Modernization Playbooks
- name: Cloud Adoption (Cloud Smart)
- name: Federal IT Workforce Development
- name: Federal Identity, Credential, and Access Management (FICAM)
- name: Open Government and Data Sharing
finops:
- name: Chief Information Officers Council Finops
  service_category: ''
  slug: chief-information-officers-council-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chief-information-officers-council.png
layout: provider
modified: '2026-09-05'
name: Chief Information Officers Council
nav: Providers
network: true
overview: Chief Information Officers Council publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CIO, Cloud, Cybersecurity, E-Government, and Federal-Government.
plans:
- name: Chief Information Officers Council Plans Pricing
  plan_count: 0
  slug: chief-information-officers-council-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Chief Information Officers Council Rate Limits
  slug: chief-information-officers-council-rate-limits
score:
  band: emerging
  composite: 11.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 0.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 18.4
    commercial_clarity: 18.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 18.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/chief-information-officers-council/refs/heads/main/screenshots/chief-information-officers-council-2026-06-20T174309.png
security:
- kind: domain-security
  name: Chief Information Officers Council Domain Security
  slug: chief-information-officers-council-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chief-information-officers-council
tags:
- CIO
- Cloud
- Cybersecurity
- E-Government
- Federal-Government
- IT Modernization
- Information Technology
- Interagency Council
- OMB
- Public Sector
use_cases:
- name: Federal IT Modernization
- name: Cloud Migration and Adoption
- name: Cybersecurity Posture Improvement
- name: Federal IT Workforce Development
- name: Cross-Agency IT Best Practice Sharing
- name: FedRAMP Authorization Coordination
- name: Identity, Credential, and Access Management
- name: Federal Data Strategy Implementation
website: https://www.councils.gov/cioc
---
