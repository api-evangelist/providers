---
access_model:
  confidence: high
  label: Free · partially keyless
  onboarding: unknown
  pricing: free
  public: true
  source:
  - examples/iit-bombay-instiapp-examples.yml
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 19.2
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: 'The IIT Bombay Computer Centre''s central identity provider, and the credential every institutional service sits behind. It publishes a live OpenID Connect Discovery 1.0 document and a JWKS: issuer htt'
  name: IITB Central SSO — OpenID Connect
  slug: sso-oidc
- description: An OAuth 2.0 (RFC 6749) identity and profile API operated by the IIT Bombay Students' Gymkhana, with ten separately-consented scopes covering SSO id, name, picture, sex, LDAP username and e-mail, phon
  name: Gymkhana Profiles OAuth API
  slug: gymkhana-profiles
- description: The IIT Bombay Central Library institutional repository, running DSpace over theses, journal articles and conference papers. Its OAI-PMH 2.0 harvesting interface is the surface of interest and it is N
  name: DSpace Institutional Repository (Central Library)
  slug: dspace-oai-pmh
- description: A session-based Single Sign-On service maintained by the Institute Technical Council for authenticating IIT Bombay users in student and club projects. A redirect-based ssocall flow returns an access i
  name: ITC Single Sign-On
  slug: itc-sso
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The achievements API from Indian Institute of Technology Bombay — 2 operation(s) for achievements.
  name: Indian Institute of Technology Bombay Achievements API
  slug: iit-bombay-achievements-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The achievements-offer API from Indian Institute of Technology Bombay — 2 operation(s) for achievements-offer.
  name: Indian Institute of Technology Bombay Achievements Offer API
  slug: iit-bombay-achievements-offer-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The alumni_login API from Indian Institute of Technology Bombay — 1 operation(s) for alumni_login.
  name: Indian Institute of Technology Bombay Alumni Login API
  slug: iit-bombay-alumni-login-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The alumni_otp_conf API from Indian Institute of Technology Bombay — 1 operation(s) for alumni_otp_conf.
  name: Indian Institute of Technology Bombay Alumni Otp Conf API
  slug: iit-bombay-alumni-otp-conf-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The bans API from Indian Institute of Technology Bombay — 2 operation(s) for bans.
  name: Indian Institute of Technology Bombay Bans API
  slug: iit-bombay-bans-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The bodies API from Indian Institute of Technology Bombay — 5 operation(s) for bodies.
  name: Indian Institute of Technology Bombay Bodies API
  slug: iit-bombay-bodies-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The buy API from Indian Institute of Technology Bombay — 6 operation(s) for buy.
  name: Indian Institute of Technology Bombay Buy API
  slug: iit-bombay-buy-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The calendar API from Indian Institute of Technology Bombay — 11 operation(s) for calendar.
  name: Indian Institute of Technology Bombay Calendar API
  slug: iit-bombay-calendar-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The check API from Indian Institute of Technology Bombay — 1 operation(s) for check.
  name: Indian Institute of Technology Bombay Check API
  slug: iit-bombay-check-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The communities API from Indian Institute of Technology Bombay — 2 operation(s) for communities.
  name: Indian Institute of Technology Bombay Communities API
  slug: iit-bombay-communities-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The delete API from Indian Institute of Technology Bombay — 1 operation(s) for delete.
  name: Indian Institute of Technology Bombay Delete API
  slug: iit-bombay-delete-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The events API from Indian Institute of Technology Bombay — 5 operation(s) for events.
  name: Indian Institute of Technology Bombay Events API
  slug: iit-bombay-events-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The external_blog API from Indian Institute of Technology Bombay — 1 operation(s) for external_blog.
  name: Indian Institute of Technology Bombay External Blog API
  slug: iit-bombay-external-blog-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The get_all_user_tags API from Indian Institute of Technology Bombay — 1 operation(s) for get_all_user_tags.
  name: Indian Institute of Technology Bombay Get All User Tags API
  slug: iit-bombay-get-all-user-tags-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The get_bodies API from Indian Institute of Technology Bombay — 2 operation(s) for get_bodies.
  name: Indian Institute of Technology Bombay Get Bodies API
  slug: iit-bombay-get-bodies-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The get_notifications API from Indian Institute of Technology Bombay — 1 operation(s) for get_notifications.
  name: Indian Institute of Technology Bombay Get Notifications API
  slug: iit-bombay-get-notifications-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The getEncr API from Indian Institute of Technology Bombay — 1 operation(s) for getencr.
  name: Indian Institute of Technology Bombay Get Encr API
  slug: iit-bombay-getencr-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The getUserMess API from Indian Institute of Technology Bombay — 1 operation(s) for getusermess.
  name: Indian Institute of Technology Bombay Get User Mess API
  slug: iit-bombay-getusermess-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The interests API from Indian Institute of Technology Bombay — 1 operation(s) for interests.
  name: Indian Institute of Technology Bombay Interests API
  slug: iit-bombay-interests-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The internship API from Indian Institute of Technology Bombay — 5 operation(s) for internship.
  name: Indian Institute of Technology Bombay Internship API
  slug: iit-bombay-internship-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The list_all API from Indian Institute of Technology Bombay — 1 operation(s) for list_all.
  name: Indian Institute of Technology Bombay List All API
  slug: iit-bombay-list-all-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The list_body API from Indian Institute of Technology Bombay — 1 operation(s) for list_body.
  name: Indian Institute of Technology Bombay List Body API
  slug: iit-bombay-list-body-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The lnf API from Indian Institute of Technology Bombay — 2 operation(s) for lnf.
  name: Indian Institute of Technology Bombay Lnf API
  slug: iit-bombay-lnf-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The locations API from Indian Institute of Technology Bombay — 2 operation(s) for locations.
  name: Indian Institute of Technology Bombay Locations API
  slug: iit-bombay-locations-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The login API from Indian Institute of Technology Bombay — 2 operation(s) for login.
  name: Indian Institute of Technology Bombay Login API
  slug: iit-bombay-login-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The logout API from Indian Institute of Technology Bombay — 1 operation(s) for logout.
  name: Indian Institute of Technology Bombay Logout API
  slug: iit-bombay-logout-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The mess API from Indian Institute of Technology Bombay — 1 operation(s) for mess.
  name: Indian Institute of Technology Bombay Mess API
  slug: iit-bombay-mess-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The my_events API from Indian Institute of Technology Bombay — 1 operation(s) for my_events.
  name: Indian Institute of Technology Bombay My Events API
  slug: iit-bombay-my-events-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The nearest API from Indian Institute of Technology Bombay — 1 operation(s) for nearest.
  name: Indian Institute of Technology Bombay Nearest API
  slug: iit-bombay-nearest-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The news_feed API from Indian Institute of Technology Bombay — 1 operation(s) for news_feed.
  name: Indian Institute of Technology Bombay News Feed API
  slug: iit-bombay-news-feed-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The notifications API from Indian Institute of Technology Bombay — 2 operation(s) for notifications.
  name: Indian Institute of Technology Bombay Notifications API
  slug: iit-bombay-notifications-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The pass_login API from Indian Institute of Technology Bombay — 1 operation(s) for pass_login.
  name: Indian Institute of Technology Bombay Pass Login API
  slug: iit-bombay-pass-login-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The perform_action API from Indian Institute of Technology Bombay — 1 operation(s) for perform_action.
  name: Indian Institute of Technology Bombay Perform Action API
  slug: iit-bombay-perform-action-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The placement_blog API from Indian Institute of Technology Bombay — 1 operation(s) for placement_blog.
  name: Indian Institute of Technology Bombay Placement Blog API
  slug: iit-bombay-placement-blog-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The placementblogs API from Indian Institute of Technology Bombay — 5 operation(s) for placementblogs.
  name: Indian Institute of Technology Bombay Placementblogs API
  slug: iit-bombay-placementblogs-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The popup-notification API from Indian Institute of Technology Bombay — 2 operation(s) for popup-notification.
  name: Indian Institute of Technology Bombay Popup Notification API
  slug: iit-bombay-popup-notification-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The query API from Indian Institute of Technology Bombay — 2 operation(s) for query.
  name: Indian Institute of Technology Bombay Query API
  slug: iit-bombay-query-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The resend_alumni_otp API from Indian Institute of Technology Bombay — 1 operation(s) for resend_alumni_otp.
  name: Indian Institute of Technology Bombay Resend Alumni Otp API
  slug: iit-bombay-resend-alumni-otp-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The roles API from Indian Institute of Technology Bombay — 2 operation(s) for roles.
  name: Indian Institute of Technology Bombay Roles API
  slug: iit-bombay-roles-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The search API from Indian Institute of Technology Bombay — 2 operation(s) for search.
  name: Indian Institute of Technology Bombay Search API
  slug: iit-bombay-search-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The shortestpath API from Indian Institute of Technology Bombay — 1 operation(s) for shortestpath.
  name: Indian Institute of Technology Bombay Shortestpath API
  slug: iit-bombay-shortestpath-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The test API from Indian Institute of Technology Bombay — 1 operation(s) for test.
  name: Indian Institute of Technology Bombay Test API
  slug: iit-bombay-test-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The training_blog API from Indian Institute of Technology Bombay — 1 operation(s) for training_blog.
  name: Indian Institute of Technology Bombay Training Blog API
  slug: iit-bombay-training-blog-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The upload API from Indian Institute of Technology Bombay — 2 operation(s) for upload.
  name: Indian Institute of Technology Bombay Upload API
  slug: iit-bombay-upload-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The user-me API from Indian Institute of Technology Bombay — 10 operation(s) for user-me.
  name: Indian Institute of Technology Bombay User Me API
  slug: iit-bombay-user-me-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The user-tags API from Indian Institute of Technology Bombay — 1 operation(s) for user-tags.
  name: Indian Institute of Technology Bombay User Tags API
  slug: iit-bombay-user-tags-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The users API from Indian Institute of Technology Bombay — 1 operation(s) for users.
  name: Indian Institute of Technology Bombay Users API
  slug: iit-bombay-users-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The venter API from Indian Institute of Technology Bombay — 7 operation(s) for venter.
  name: Indian Institute of Technology Bombay Venter API
  slug: iit-bombay-venter-api
- baseURL: https://gymkhana.iitb.ac.in/instiapp/api
  baseurl_source: declared
  description: The verifier_events API from Indian Institute of Technology Bombay — 1 operation(s) for verifier_events.
  name: Indian Institute of Technology Bombay Verifier Events API
  slug: iit-bombay-verifier-events-api
- baseURL: https://sso.iitb.ac.in
  baseurl_source: declared
  description: The Community Posts API from Indian Institute of Technology Bombay — 3 operation(s) for community posts.
  name: Indian Institute of Technology Bombay Community Posts API
  slug: iit-bombay-community-posts-api
artifact_total: 64
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/DevCom-IITB/instiapp-api/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://www.iitb.ac.in/
- group: docs
  title: ''
  type: APIReference
  url: https://gymkhana.iitb.ac.in/instiapp/api/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://gymkhana.iitb.ac.in/profiles/doc/
- group: other
  title: ''
  type: IdentityFederation
  url: https://sso.iitb.ac.in/.well-known/openid-configuration
- group: other
  title: ''
  type: ResearchRepository
  url: https://dspace.library.iitb.ac.in/
- group: build
  title: ''
  type: LibraryCatalog
  url: https://www.library.iitb.ac.in/
- group: learn
  title: ''
  type: CourseCatalog
  url: https://asc.iitb.ac.in/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DevCom-IITB
- group: operate
  title: ''
  type: Support
  url: https://github.com/DevCom-IITB/instiapp-api/issues
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.iitb.ac.in/credits-disclaimer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/indian-institute-of-technology-bombay/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/iit-bombay/refs/heads/main/security/iit-bombay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/iit-bombay-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/iit-bombay/refs/heads/main/plans/iit-bombay-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/iit-bombay-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/iit-bombay/refs/heads/main/rate-limits/iit-bombay-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/iit-bombay-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/iit-bombay/refs/heads/main/finops/iit-bombay-finops.yml
  title: ''
  type: FinOps
  url: finops/iit-bombay-finops.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/iit-bombay/refs/heads/main/review.yml
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'The Indian Institute of Technology Bombay (IIT Bombay), founded in 1958 at Powai, Mumbai, is one of India''s premier engineering and research institutions and one of the very few universities in this catalog that actually publishes a first-party, machine-readable API contract of its own. It operates no central developer portal and no institutional API programme, and there is no course catalog, registrar, open-data or research-computing API in public view. What it does run — and what almost every peer institution does not — is a live OpenAPI-described campus-life API, InstiApp, served from its own host at gymkhana.iitb.ac.in with an autogenerated 112-path specification, an institutional contact address and AGPL-3.0 source published by the Developers'' Community. Alongside it sit two institution-operated identity surfaces: the Computer Centre''s central OpenID Connect provider at sso.iitb.ac.in, which publishes a live discovery document and JWKS, and the Students'' Gymkhana OAuth
  2.0 Profiles service with ten documented consent scopes, access to which is restricted to applications hosted on Gymkhana infrastructure. The Central Library runs a DSpace institutional repository whose OAI-PMH endpoint is currently denied at the web-server layer. A fourth surface, the Institute Technical Council''s SSO, is run by an IIT Bombay student body but on a domain the institution does not own, and is recorded as a tenant relationship rather than credited to the institution.'
finops:
- name: Iit Bombay Finops
  service_category: Education
  slug: iit-bombay-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iit-bombay.png
json_schemas:
- name: IIT Bombay InstiApp API — data model
  property_count: 0
  slug: iit-bombay-instiapp-schemas
jsonld:
- class_count: 29
  name: Iit Bombay Context
  property_count: 0
  slug: iit-bombay-context
- class_count: 0
  name: Iit Bombay Surfaces Context
  property_count: 0
  slug: iit-bombay-surfaces
layout: provider
modified: '2026-08-30'
name: Indian Institute of Technology Bombay
nav: Providers
network: true
overview: 'Indian Institute of Technology Bombay publishes 50 APIs on the [APIs.io](https://apis.io/) network, including Achievements API, Achievements Offer API, Alumni Login API, and 47 more. Tagged areas include University, Higher Education, Education, India, and Institute of Technology.


  The Indian Institute of Technology Bombay catalog on APIs.io includes 2 JSON-LD contexts and 1 Spectral governance ruleset.


  Indian Institute of Technology Bombay''s developer surface includes API reference, documentation, support, and 14 more developer resources.'
plans:
- name: Iit Bombay Plans Pricing
  plan_count: 2
  slug: iit-bombay-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 1
  name: Iit Bombay Rate Limits
  slug: iit-bombay-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: Indian Institute of Technology Bombay API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: iit-bombay-rules
scopes:
- name: Iit Bombay Scopes
  scope_count: 0
  slug: iit-bombay-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 1.3
  facets:
    access_clarity: 39.5
    contract_governance: 29.5
    contract_quality: 63.3
    developer_ergonomics: 33.3
    discoverability: 63.0
    operational_transparency: 23.7
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 45.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 50
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 57.4
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/iit-bombay/refs/heads/main/screenshots/iit-bombay-2026-06-20T183229.png
security:
- kind: authentication
  name: Iit Bombay Authentication
  slug: iit-bombay-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Iit Bombay Domain Security
  slug: iit-bombay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: iit-bombay
tags:
- University
- Higher Education
- Education
- India
- Institute of Technology
- Research
- Identity
- SSO
- OpenID Connect
- Campus Life
- Research Repository
- Open-Source
website: https://www.iitb.ac.in/
---
