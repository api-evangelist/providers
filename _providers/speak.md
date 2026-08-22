---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: true
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
  score: 11.1
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: Production application backend for the Speak language-learning app. It is an OAuth2/OIDC issuer (token endpoint at /v1/auth/token, JWKS published) serving the iOS, Android, and web clients. Not docume
  name: Speak API
  slug: speak-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://www.speak.com/
- group: company
  title: ''
  type: Blog
  url: https://www.speak.com/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.speak.com/en/
- group: start
  title: ''
  type: SignUp
  url: https://app.speak.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://usespeak.notion.site/Speak-s-Privacy-Policy-29b9293ddabc48bcb1b059bc84e8f490
- group: commercial
  title: ''
  type: TermsOfService
  url: https://usespeak.notion.site/Speak-s-Terms-of-Service-5a9643bc1e774a76afb1930abec99f39
- group: agent
  title: ''
  type: WellKnown
  url: well-known/speak-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/speak-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/speak-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/speak-authentication.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/speak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/speak-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/speak-domain-security.yml
created: '2026-07-17'
description: Speak (Speakeasy Labs, Inc.) is an AI-powered language learning application focused on spoken fluency rather than grammar drills or vocabulary memorization. Its proprietary "Speak Method" has learners study real phrases, practice them across contexts, and then apply them in back-and-forth conversation with an AI tutor that gives real-time pronunciation and fluency feedback. Speak teaches Spanish, French, Korean, Japanese, Italian, German, and Chinese, plus English for non-English speakers, and offers B2B language training for organizations across Korea, Japan, Spain, Taiwan, and France. The company is backed by Accel and the OpenAI Startup Fund and partners with OpenAI. Speak runs a production application backend at api.usespeak.com (an OAuth2/OIDC issuer) but does not publish a public developer API, OpenAPI specification, or SDKs; the surfaces below were discovered from the company's public well-known and llms.txt endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/speak.png
layout: provider
modified: '2026-07-21'
name: Speak
nav: Providers
network: true
overview: 'Speak publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Language Learning, Education, and EdTech.


  Speak''s developer surface includes engineering blog, signup flow, authentication, and 10 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 17.9
  delta: -2.5
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 40.7
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Speak Authentication
  slug: speak-authentication
  summary_line: oauth2/openIdConnect · 1 scheme
- kind: domain-security
  name: Speak Domain Security
  slug: speak-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Speak Vulnerability Disclosure
  slug: speak-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: speak
tags:
- Company
- Ai
- Language Learning
- Education
- EdTech
- Speech
- Conversational AI
- Mobile
website: https://www.speak.com/
---
