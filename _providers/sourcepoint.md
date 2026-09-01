---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.9
  scored_at: '2026-09-01'
api_count: 14
apis:
- description: The GDPR reporting API API from Sourcepoint — 2 operation(s) for gdpr reporting api.
  name: Sourcepoint GDPR reporting API
  slug: sourcepoint-gdpr-reporting-api-api
- description: The GDPR Standard end-user consent status API from Sourcepoint — 2 operation(s) for gdpr standard end-user consent status.
  name: Sourcepoint GDPR Standard end-user consent status API
  slug: sourcepoint-gdpr-standard-end-user-consent-status-api
- description: The GDPR Standard vendor list API from Sourcepoint — 2 operation(s) for gdpr standard vendor list.
  name: Sourcepoint GDPR Standard vendor list API
  slug: sourcepoint-gdpr-standard-vendor-list-api
- description: The GDPR TCF end-user consent status API from Sourcepoint — 3 operation(s) for gdpr tcf end-user consent status.
  name: Sourcepoint GDPR TCF end-user consent status API
  slug: sourcepoint-gdpr-tcf-end-user-consent-status-api
- description: The GDPR TCF vendor list API from Sourcepoint — 3 operation(s) for gdpr tcf vendor list.
  name: Sourcepoint GDPR TCF vendor list API
  slug: sourcepoint-gdpr-tcf-vendor-list-api
- description: The Global Enterprise end-user consent status API from Sourcepoint — 2 operation(s) for global enterprise end-user consent status.
  name: Sourcepoint Global Enterprise end-user consent status API
  slug: sourcepoint-global-enterprise-end-user-consent-status-api
- description: The Preferences end-user history API from Sourcepoint — 2 operation(s) for preferences end-user history.
  name: Sourcepoint Preferences end-user history API
  slug: sourcepoint-preferences-end-user-history-api
- description: The U.S. Multi-State Privacy end-user consent status API from Sourcepoint — 3 operation(s) for u.s. multi-state privacy end-user consent status.
  name: Sourcepoint U.S. Multi-State Privacy end-user consent status API
  slug: sourcepoint-u-s-multi-state-privacy-end-user-consent-status-api
- description: The U.S. Multi-State Privacy reporting API API from Sourcepoint — 2 operation(s) for u.s. multi-state privacy reporting api.
  name: Sourcepoint U.S. Multi-State Privacy reporting API
  slug: sourcepoint-u-s-multi-state-privacy-reporting-api-api
artifact_total: 38
collections:
- collection_type: open
  name: Sourcepoint GDPR Standard API
  slug: open-sourcepoint-gdpr-standard
- collection_type: open
  name: Sourcepoint GDPR TCF API
  slug: open-sourcepoint-gdpr-tcf
- collection_type: open
  name: Sourcepoint Global Enterprise API
  slug: open-sourcepoint-global-enterprise
- collection_type: open
  name: Preferences API
  slug: open-sourcepoint-preferences
- collection_type: open
  name: Sourcepoint Reporting GDPR API
  slug: open-sourcepoint-reporting-gdpr
- collection_type: open
  name: Sourcepoint Reporting U.S. Multi-State Privacy API
  slug: open-sourcepoint-reporting-usnat
- collection_type: open
  name: Sourcepoint U.S. Multi-State Privacy API
  slug: open-sourcepoint-usnat
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcepoint-gdpr-tcf-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcepoint-gdpr-standard-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcepoint-usnat-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcepoint-global-enterprise-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcepoint-preferences-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcepoint-reporting-gdpr-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/sourcepoint-reporting-usnat-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sourcepoint-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sourcepoint-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sourcepoint.com
- group: start
  title: ''
  type: Portal
  url: https://docs.sourcepoint.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://sourcepoint-public-api.readme.io/reference
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4416092045587-GDPR-TCF-implementation-guide-web
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4405397484307-Event-callbacks-CMP
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4405412419731-Client-configuration-parameters
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/4403274791699-Authenticated-consent
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/6490142709139-Native-App-Messages-App-setup
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sourcepoint.com/hc/en-us/articles/25872524725267-Google-Consent-Mode-2-0-GDPR-TCF-web
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/cmp-2/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/diagnose/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/dsar/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/marketing-preferences/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/universal-consent-and-preferences
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/privacy-lens/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/ott-ctv/
- group: other
  title: ''
  type: Product
  url: https://sourcepoint.com/cmp-for-mobile-apps/
- group: commercial
  title: ''
  type: Pricing
  url: https://hs.sourcepoint.com/pricing
- group: start
  title: ''
  type: Signup
  url: https://www.sourcepoint.com/schedule-a-demo/
- group: company
  title: ''
  type: Blog
  url: https://www.sourcepoint.com/blog/
- group: company
  title: ''
  type: News
  url: https://www.sourcepoint.com/news/
- group: company
  title: ''
  type: About
  url: https://www.sourcepoint.com/about-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SourcePointUSA
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/ios-cmp-app
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/android-cmp-app
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/react-native-sourcepoint-cmp
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/unity-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/sp-roku-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/SP_HTML5_OTT
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/mobile-core
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/diagnose-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/SourcePointUSA/es3-QR-SDK-develop
- group: build
  title: ''
  type: Plugin
  url: https://github.com/SourcePointUSA/sp-wordpress-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/SourcePointUSA/sp-magento-plugin
- group: build
  title: ''
  type: Plugin
  url: https://github.com/SourcePointUSA/GTM-GCM-Template
- group: build
  title: ''
  type: Tools
  url: https://github.com/SourcePointUSA/sdks-auth-consent-test-page
- group: build
  title: ''
  type: Tools
  url: https://github.com/SourcePointUSA/FORK-iabgpp-es
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sourcepoint
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sourcepoint
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sourcepoint-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sourcepoint-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/sourcepoint-api-catalog.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sourcepoint-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sourcepoint-tool-crosswalk.yml
- group: build
  title: ''
  type: Packages
  url: packages/sourcepoint-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sourcepoint-packages.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sourcepoint-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.sourcepoint.com/trust-and-security/
- group: auth
  title: ''
  type: TrustCenter
  url: security/sourcepoint-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sourcepoint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.sourcepoint.com/trust-and-security/
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sourcepoint-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sourcepoint-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sourcepoint-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/sourcepoint-changelog.yml
- group: design
  title: ''
  type: Components
  url: components/sourcepoint-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sourcepoint-data-model.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sourcepoint-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sourcepoint-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  title: ''
  type: APIReference
  url: https://sourcepoint-public-api.readme.io/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://sourcepoint-public-api.readme.io/reference/welcome-to-the-sourcepoint-api-hub
- group: operate
  title: ''
  type: HelpCenter
  url: https://docs.sourcepoint.com/hc/en-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sourcepoint.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sourcepoint.com/privacy-policy/
- group: commercial
  title: ''
  type: PrivacyNotice
  url: https://www.sourcepoint.com/privacy-notice/
- group: start
  title: ''
  type: Login
  url: https://portal.sourcepoint.com
- group: company
  title: ''
  type: Press
  url: https://www.sourcepoint.com/press/
created: '2026-05-25'
description: Sourcepoint is a New York City-headquartered enterprise privacy and consent management technology company founded in 2015 by Ben Barokas and Brian Kane. The platform began as an ad-block recovery solution for publishers and evolved into a Consent Management Platform (CMP) used by leading global publishers and brands — including Axel Springer, Bauer Media, CNN International, Future, Haymarket, LADBible, Autotrader, and Ancestry — to handle GDPR, CCPA, U.S. Multi-State Privacy (USNAT), LGPD, and other regulations under the IAB TCF v2.2 and IAB Global Privacy Platform (GPP) frameworks. Sourcepoint products include the multi-campaign CMP across web, AMP, mobile (iOS, Android, React Native), Unity, Roku, HTML5 OTT and CTV surfaces, Compliance Monitoring (Diagnose), DSAR Handling, Universal Consent & Preferences, Marketing Preferences, Privacy Lens, and tooling for ad-block recovery. The Sourcepoint Public API exposes REST endpoints for GDPR TCF, GDPR Standard, U.S. Multi-State Privacy,
  Global Enterprise consent, and Preferences history, plus reporting endpoints for dashboards. Sourcepoint technology powers over 30 billion consumer touchpoints per month. In July 2025, Sourcepoint was acquired by Paris-based Didomi (a Marlin Equity Partners portfolio company) to consolidate global consent management; Sourcepoint continues to operate under its existing brand and developer surface during integration.
features:
- Multi-campaign Consent Management Platform across web, AMP, mobile, OTT, CTV, and gaming surfaces
- IAB TCF v2.2 support including Transaction Receipts, Legal Preferences, and sensitive-data opt-in
- IAB Global Privacy Platform (GPP) support for U.S. Multi-State Privacy (USNAT) sections
- GDPR, CCPA / U.S. Multi-State Privacy, LGPD, and global multi-regulation orchestration
- Universal Consent & Preferences for unified first-party preference data
- Authenticated Consent for syncing an end-user's preferences across devices
- Diagnose compliance monitoring of vendors, trackers, and data flows on a property
- DSAR Handling for data subject access and erasure workflows
- Marketing Preferences and Privacy Lens measurement
- Ad-block recovery heritage for publisher monetization
- Google Consent Mode 2.0 integration and GTM template
- Native mobile SDKs for iOS (Swift / CocoaPods / SPM / XCFramework), Android (Kotlin / Maven Central), React Native, Unity, Roku, and HTML5 OTT
- Web messaging via cdn.privacy-mgmt.com/unified/wrapperMessagingWithoutDetection.js with optional CNAME subdomain
- Public REST API for GDPR TCF, GDPR Standard, U.S. Multi-State Privacy, Global Enterprise, Preferences, and Reporting
- Approximately 30 billion consumer touchpoints powered per month
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sourcepoint.png
layout: provider
mcp_servers:
- description: ''
  name: Sourcepoint MCP Server
  slug: sourcepoint-mcp-server
modified: '2026-08-12'
name: Sourcepoint
nav: Providers
network: true
overview: 'Sourcepoint publishes 9 APIs on the [APIs.io](https://apis.io/) network, including GDPR reporting API, GDPR Standard end-user consent status API, GDPR Standard vendor list API, and 6 more. Tagged areas include Privacy, Consent Management, Consent Management Platform, CMP, and GDPR.


  Sourcepoint''s developer surface includes authentication, developer portal, documentation, pricing, signup flow, engineering blog, product news, and 70 more developer resources.'
plans:
- name: Sourcepoint Plans Pricing
  plan_count: 3
  slug: sourcepoint-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Sourcepoint Rate Limits
  slug: sourcepoint-rate-limits
score:
  band: strong
  composite: 55.6
  coverage:
    artifact_dirs: 21
    catalog_gap: 63.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 45.7
    developer_ergonomics: 64.9
    discoverability: 81.5
    governance: 18.2
    operational_transparency: 28.9
  previous_composite: 55.6
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sourcepoint/refs/heads/main/screenshots/sourcepoint-2026-06-20T194225.png
security:
- kind: authentication
  name: Sourcepoint Authentication
  slug: sourcepoint-authentication
  summary_line: apiKey/none · 2 schemes
- kind: domain-security
  name: Sourcepoint Domain Security
  slug: sourcepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sourcepoint Vulnerability Disclosure
  slug: sourcepoint-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Sourcepoint Trust Center
  slug: sourcepoint-trust-center
  summary_line: ISO/IEC 27001, ISO/IEC 27701
slug: sourcepoint
tags:
- Privacy
- Consent Management
- Consent Management Platform
- CMP
- GDPR
- CCPA
- LGPD
- IAB TCF
- IAB GPP
- USNAT
- DSAR
- Adblock Recovery
- Compliance Monitoring
- Publisher Technology
- AdTech
- MarTech
- Privacy Engineering
- CTV
- OTT
- Mobile SDK
- Web SDK
website: https://www.sourcepoint.com
---
