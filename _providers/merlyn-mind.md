---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: 0.2
  score: 5.4
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 5
common:
- group: auth
  title: ''
  type: Security
  url: security/merlyn-mind-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/merlyn-mind-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/merlyn-mind-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: security/merlyn-mind-trust-center.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/merlyn-mind-llms.txt
- group: auth
  title: ''
  type: TrustCenter
  url: security/merlyn-mind-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/merlyn-mind-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.merlyn.org/
- group: company
  title: ''
  type: Blog
  url: https://www.merlyn.org/blogs
- group: operate
  title: ''
  type: Support
  url: https://www.merlyn.org/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://merlynorigin.zendesk.com/hc/en-us
- group: start
  title: ''
  type: Login
  url: https://portal.merlyn.org/
- group: start
  title: ''
  type: Console
  url: https://manage.merlyn.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.merlyn.org/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.merlyn.org/privacy-policy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/MerlynMind
coverage:
  checked: '2026-08-25'
  detail: Merlyn Mind sells Merlyn Origin and Merlyn Display as finished classroom products and runs no developer program at all — its 97-URL sitemap contains no developer, docs or API page, and developer/docs/api.merlyn.org do not resolve; the only REST API it operates, web.rest-api.merlyn.org, is an undocumented AWS API Gateway backing its own console and teacher portal that answers every anonymous request with 403 "Missing Authentication Token".
  evidence:
  - status: 200
    url: https://www.merlyn.org/sitemap.xml
  - status: 403
    url: https://web.rest-api.merlyn.org/openapi.json
  - status: 404
    url: https://www.merlyn.org/llms.txt
  - status: 404
    url: https://www.merlyn.org/.well-known/api-catalog
  reason: no-developer-program
  state: none
created: '2026-08-25'
description: 'Merlyn Mind is a New York-based deep-tech generative AI company, founded in 2018, that builds domain-specific AI for K-12 education. Its products are Merlyn Origin, a software AI assistant that runs on a teacher''s classroom computer, and Merlyn Display, the same assistant embedded in interactive flat panels from partners such as Promethean and Newline. The company trained its own education-specific large language models and published several of them openly on Hugging Face (merlyn-education-safety, merlyn-education-corpus-qa, merlyn-education-teacher-assistant), and runs an AI Labs research group that publishes at NeurIPS and other conferences. Merlyn integrates with classroom tooling including the Canvas LMS. Merlyn Mind was acquired by Mynd.ai, Inc. (NYSE American, MYND), the parent of Promethean, in a deal completed 9 September 2025, and continues to operate under the merlyn.org brand with offices in New York, Irvine and Bangalore. Merlyn Mind publishes no public developer
  program: there is no developer portal, no API reference, no SDK and no machine-readable contract.'
image: https://cdn.prod.website-files.com/653ff772c8cabb196596168a/653ff772c8cabb196596191e_merlynorg.svg
layout: provider
modified: '2026-08-25'
name: Merlyn Mind
nav: Providers
network: true
overview: 'Merlyn Mind is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Education, EdTech, and K-12.


  Merlyn Mind''s developer surface includes engineering blog, support, developer console, and 13 more developer resources.'
plans:
- name: Merlyn Mind Plans Pricing
  plan_count: 0
  slug: merlyn-mind-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 0
  name: Merlyn Mind Rate Limits
  slug: merlyn-mind-rate-limits
score:
  band: emerging
  composite: 23.9
  coverage:
    artifact_dirs: 7
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 43.4
    commercial_clarity: 43.4
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.4
    governance: 18.2
    operational_transparency: 13.2
  previous_composite: 23.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: coppa
    - jurisdiction: US
      standard: ferpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 55.6
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Merlyn Mind Domain Security
  slug: merlyn-mind-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Merlyn Mind Vulnerability Disclosure
  slug: merlyn-mind-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Merlyn Mind Trust Center
  slug: merlyn-mind-trust-center
  summary_line: SOC 2, SOC 3
slug: merlyn-mind
tags:
- Company
- Artificial Intelligence
- Education
- EdTech
- K-12
- Large Language Models
- Voice Assistant
- Classroom Technology
- Machine-Learning
- Responsible AI
website: https://www.merlyn.org/
---
