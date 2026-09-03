---
access_model:
  confidence: high
  label: Free · Institutional affiliation required
  onboarding: unknown
  pricing: free
  public: false
  source:
  - probed
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 5.0
  scored_at: '2026-09-02'
api_count: 5
apis:
- description: HKBU's own SAML 2.0 identity provider, entityID https://buidp01.hkbu.edu.hk/idp/shibboleth, registered in eduGAIN by the Hong Kong Access Federation (HKAF) since 2018-03-14 with scope hkbu.edu.hk. The
  name: HKBU Identity Federation (Shibboleth IdP / SAML 2.0 metadata)
  slug: identity-federation
- description: HKBU runs its own generative-AI gateway at genai.hkbu.edu.hk, fronting third-party models (Anthropic, Google, Meta AI, OpenAI) for staff and students. Probing on 2026-08-30 found a live REST surface a
  name: HKBU GenAI Platform API (undocumented, key-gated)
  slug: genai-platform-api
- description: 'HKBU self-hosts Moodle at buelearning.hkbu.edu.hk on its own registrable domain. It publishes a live IMS LTI 1.3 Advantage tool-platform key set at /mod/lti/certs.php (HTTP 200, one RSA RS256 signing '
  name: HKBU Moodle — IMS LTI 1.3 platform + web services
  slug: moodle-lti-platform
- description: Backend host serving the official HKBU Mobile application (mapp-api.hkbu.edu.hk). The host resolves over TLS 1.3 with HSTS and serves app support content such as the app privacy notice (HTTP 200), but
  name: HKBU Mobile App Backend (gated)
  slug: mobile-app-backend
- description: 'HKBU Scholars is HKBU''s research information portal and institutional repository, and it is an Elsevier Pure tenancy: scholars.hkbu.edu.hk is a CNAME to hkbu.elsevierpure.com, and repository.hkbu.edu.'
  name: HKBU Scholars — Elsevier Pure tenancy (tenant relationship, contract not HKBU's)
  slug: scholars-pure-tenancy
artifact_total: 10
common:
- group: company
  title: ''
  type: Website
  url: https://www.hkbu.edu.hk/
- group: company
  title: ''
  type: Blog
  url: https://www.hkbu.edu.hk/en/whats-new.html
- group: other
  title: ''
  type: IdentityFederation
  url: https://buidp01.hkbu.edu.hk/idp/shibboleth
- group: build
  title: ''
  type: AITooling
  url: https://genai.hkbu.edu.hk/
- group: other
  title: ''
  type: AIPolicy
  url: https://ar.hkbu.edu.hk/student-services/learning-and-teaching/learning-and-teaching-strategy-and-policies/principles-for-the-use-of-generative-ai-tools-in-teaching-and-learning-and-assessment
- group: other
  title: ''
  type: ResearchRepository
  url: https://scholars.hkbu.edu.hk/
- group: other
  title: ''
  type: OpenData
  url: https://data-hub.hkbu.edu.hk/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.hkbu.edu.hk/en/disclaimer.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bupdpo.hkbu.edu.hk/policies-and-procedures/pps-pics/
- group: operate
  title: ''
  type: Support
  url: https://ito.hkbu.edu.hk/contact-us.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/HKBUNLP
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/hong-kong-baptist-university/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/hkbaptistu
- group: design
  title: ''
  type: Conformance
  url: conformance/hong-kong-baptist-university-conformance.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/hong-kong-baptist-university-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hong-kong-baptist-university-domain-security.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/hong-kong-baptist-university-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/hong-kong-baptist-university-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/hong-kong-baptist-university-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
coverage:
  detail: 'HKBU operates four surfaces of its own and publishes a machine-readable contract for none of them. The Shibboleth/SAML 2.0 IdP metadata at buidp01.hkbu.edu.hk is fully anonymous and complete, but it is federation metadata, not an HTTP API, so it yields no OpenAPI. The GenAI Platform API and the Moodle LTI 1.3 / web-services endpoints are both live and both answer 401/400 for credentials rather than 404, proving the surfaces exist while withholding their shape; neither publishes an OpenAPI or public developer documentation. The mobile-app backend is first-party only. The one place HKBU did publish an OpenAPI — scholars.hkbu.edu.hk/ws/api — is an Elsevier Pure tenancy (scholars.hkbu.edu.hk CNAMEs to hkbu.elsevierpure.com) whose contract belongs to Elsevier and has been removed from this repository along with everything derived from it — 115 files. Two secondary institution hosts could not be read: digital.lib.hkbu.edu.hk returns a 403 "Access Denied" page to every client tried including
    a full browser User-Agent, and scholars.hkbu.edu.hk/en/ sits behind a Cloudflare interstitial. State is gated rather than none because real surfaces were confirmed live behind credentials, and rather than vendor_only because the institution-operated set is genuine.'
  evidence:
  - note: SAML 2.0 metadata, application/xml, 12,306 bytes, scope hkbu.edu.hk.
    status: 200
    url: https://buidp01.hkbu.edu.hk/idp/shibboleth
  - note: 'POST without credentials: {"message":"API key is missing or invalid."}'
    status: 401
    url: https://genai.hkbu.edu.hk/general/rest/deployments/gpt-4o-mini/chat/completions?api-version=2024-05-01-preview
  - note: POST with an api-key header returns a distinct key-validation 401.
    status: 401
    url: https://genai.hkbu.edu.hk/general/rest/deployments/gpt-4o-mini/embeddings?api-version=2024-05-01-preview
  - note: Live IMS LTI 1.3 JWKS, one RSA RS256 key.
    status: 200
    url: https://buelearning.hkbu.edu.hk/mod/lti/certs.php
  - note: OAuth2 client-credentials token endpoint, invalid_request when called bare.
    status: 400
    url: https://buelearning.hkbu.edu.hk/mod/lti/token.php
  - note: Moodle Web Services enabled; returns invalidtoken, not a 404.
    status: 200
    url: https://buelearning.hkbu.edu.hk/webservice/rest/server.php?wsfunction=core_webservice_get_site_info&moodlewsrestformat=json
  - note: Elsevier Pure contract, key-gated. Tenant surface, not HKBU's contract.
    status: 401
    url: https://scholars.hkbu.edu.hk/ws/api/524/openapi.yaml
  - note: Pure OAI-PMH endpoint present but access-restricted.
    status: 401
    url: https://scholars.hkbu.edu.hk/ws/oai?verb=Identify
  - note: Mobile backend host live; no developer documentation.
    status: 200
    url: https://mapp-api.hkbu.edu.hk/html/app_privacy_policy.html
  - note: Library digital collections return an Access Denied page to every client tried.
    status: 403
    url: https://digital.lib.hkbu.edu.hk/
  - note: OIRP Data Hub; a link surface over Power BI reports, no data API.
    status: 200
    url: https://data-hub.hkbu.edu.hk/
  - note: Empty organisation, zero public repositories; not an institutional code presence.
    status: 200
    url: https://github.com/hkbu
  reason: auth_required
  state: gated
created: '2026-06-03'
description: 'Hong Kong Baptist University (HKBU) is a publicly funded, UGC-supported research university in Hong Kong SAR. Re-profiled on 2026-08-30 under the API Evangelist university pipeline, which settles WHO OPERATES each surface before crediting any contract. HKBU operates no central developer portal, no public API catalogue and no institution-wide GitHub organisation; github.com/hkbu exists but is empty, and the only active HKBU orgs are research labs (HKBUNLP, HKBU-HPML). What HKBU does operate itself, verified by live probe, is four things: a Shibboleth/SAML 2.0 identity provider at buidp01.hkbu.edu.hk registered in eduGAIN through the Hong Kong Access Federation since 2018 and serving 12KB of signed SAML metadata anonymously; a self-built GenAI Platform whose Azure-OpenAI-shaped chat-completions and embeddings endpoints answer on genai.hkbu.edu.hk behind an api-key header, undocumented publicly; a self-hosted Moodle at buelearning.hkbu.edu.hk publishing a live IMS LTI 1.3 JWKS
  and OAuth2 token endpoint under HKBU''s own signing keys; and a first-party mobile-app backend at mapp-api.hkbu.edu.hk with no public documentation. Everything that looks like an HKBU research API is not. The HKBU Scholars portal at scholars.hkbu.edu.hk is a CNAME to hkbu.elsevierpure.com — an Elsevier Pure tenancy. The 33 OpenAPI documents previously held in this repository were Elsevier''s Pure Web Service contract 5.35.0 (info.contact pure-support@elsevier.com), the same document other Pure institutions ship, and have been removed along with everything derived from them. The data is HKBU''s; the contract is Elsevier''s, and it scores in Elsevier''s repository, not here.'
finops:
- name: Hong Kong Baptist University Finops
  service_category: Education
  slug: hong-kong-baptist-university-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hong-kong-baptist-university.png
layout: provider
modified: '2026-08-30'
name: Hong Kong Baptist University
nav: Providers
network: true
overview: 'Hong Kong Baptist University publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include University, Higher Education, Education, Hong Kong, and UGC-Funded.


  Hong Kong Baptist University''s developer surface includes engineering blog, support, GitHub presence, authentication, and 16 more developer resources.'
plans:
- name: Hong Kong Baptist University Plans Pricing
  plan_count: 2
  slug: hong-kong-baptist-university-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Hong Kong Baptist University Rate Limits
  slug: hong-kong-baptist-university-rate-limits
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 8
    catalog_gap: 61.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 18.2
    contract_quality: 4.4
    developer_ergonomics: 28.6
    discoverability: 64.8
    governance: 18.2
    operational_transparency: 26.3
  previous_composite: 33.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 61.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/hong-kong-baptist-university/refs/heads/main/screenshots/hong-kong-baptist-university-2026-06-20T182824.png
security:
- kind: authentication
  name: Hong Kong Baptist University Authentication
  slug: hong-kong-baptist-university-authentication
  summary_line: apiKey/oauth2/saml/token · 5 schemes
- kind: domain-security
  name: Hong Kong Baptist University Domain Security
  slug: hong-kong-baptist-university-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: hong-kong-baptist-university
tags:
- University
- Higher Education
- Education
- Hong Kong
- UGC-Funded
- Identity Federation
- Shibboleth
- SAML
- eduGAIN
- Learning Management
- LTI
- Artificial Intelligence
- Research Information
- Elsevier Pure
website: https://www.hkbu.edu.hk/
---
