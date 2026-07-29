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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 6
apis:
- description: REST API surfacing end-user consent operations under the GDPR using the IAB Transparency & Consent Framework (TCF v2.2). Supports retrieving end-user consent status and history by site, merging an end
  name: Sourcepoint GDPR TCF API
  slug: sourcepoint-gdpr-tcf-api
- description: 'REST API exposing GDPR consent operations outside of the IAB TCF framework for organizations that need GDPR compliance with custom vendor lists. Operations include retrieving end-user consent status, '
  name: Sourcepoint GDPR Standard API
  slug: sourcepoint-gdpr-standard-api
- description: REST API for U.S. Multi-State Privacy (USNAT) end-user consent handling, built on the IAB Global Privacy Platform (GPP) string. Supports retrieving end-user consent history, deleting consent status, o
  name: Sourcepoint U.S. Multi-State Privacy API
  slug: sourcepoint-usnat-multi-state-privacy-api
- description: REST API for the Global Enterprise consent product, providing a single multi-regulation consent surface across global properties. Supports retrieving end-user consent history, deleting consent status,
  name: Sourcepoint Global Enterprise API
  slug: sourcepoint-global-enterprise-api
- description: REST API for Universal Consent & Preferences and Marketing Preferences, letting organizations retrieve and delete an end-user's preferences history and read getUserPreferences on the web surface. Enab
  name: Sourcepoint Preferences API
  slug: sourcepoint-preferences-api
- description: REST API exposing aggregated dashboard data for GDPR and U.S. Multi-State Privacy campaigns, including pageview and message data filtered by period for dashboard and BI integration. Powers the Sourcep
  name: Sourcepoint Reporting API
  slug: sourcepoint-reporting-api
artifact_total: 22
common:
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
modified: '2026-05-25'
name: Sourcepoint
nav: Providers
network: true
overview: 'Sourcepoint publishes 6 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Privacy, Consent Management, Consent Management Platform, CMP, and GDPR.


  Sourcepoint''s developer surface includes developer portal, documentation, pricing, signup flow, engineering blog, product news, tooling, and 33 more developer resources.'
random_paper: 77
score:
  band: emerging
  composite: 16.2
  delta: -2.3
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 34.8
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 18.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sourcepoint/refs/heads/main/screenshots/sourcepoint-2026-06-20T194225.png
security:
- kind: domain-security
  name: Sourcepoint Domain Security
  slug: sourcepoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
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
