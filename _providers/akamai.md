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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: true
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 49.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 243
  human_in_the_loop: 1
  name: Akamai Agentic Access
  operation_count: 505
  slug: akamai-agentic-access
  summary_line: 505 operations · 243 acting · 1 human-in-the-loop
api_count: 204
apis:
- description: Adaptive Media Delivery supports Token Authentication. You can apply it to generate unique tokens and include them in requests for your content. Akamai validates these tokens to grant access to your m
  name: Akamai Access Revocation API
  slug: akamai-access-revocation-api
- description: The Adaptive Acceleration service takes advantage of the Server Push feature thats available with the HTTP/2 protocol, and Automatic Preconnect to increase page load speed.
  name: Akamai Adaptive Acceleration API
  slug: akamai-adaptive-acceleration-api
- description: Akamai MFA provides strong secondary authentication to cloud, on-premises, web-based, SaaS, and IaaS applicationsin addition to your primary verification mechanism, like the identity provider (IdP) sy
  name: Akamai MFA API
  slug: akamai-mfa-api
- description: The Alerts API allows you to configure notifications about significant changes to your traffic based on continual tracking by Akamais network monitoring platform. It allows you to create and modify al
  name: Akamai Alerts API
  slug: akamai-alerts-api
- description: Like API Keys and Traffic Management in Akamai Control Center, this API lets you create and manage API keys that serve as unique identifiers for API consumers. API keys exist inside top-level units ca
  name: Akamai API Keys and Traffic Management API
  slug: akamai-api-keys-and-traffic-management-api
- description: This API allows the Licensed CDN (LCDN) Operator to create sites, nodes, and attribute types for LCDN or LMS products on the Aura platform. This API does not support the deployment of individual produ
  name: Akamai Aura Infrastructure API
  slug: akamai-aura-infrastructure-api
- description: This API allows the LCDN Operator or Content Provider to purge content on the Aura LCDN. Purging removes outdated or unwanted content. Content can be purged one asset at a time, as a list of assets, o
  name: Akamai Aura LCDN Content Control API
  slug: akamai-aura-lcdn-content-control-api
- description: This API allows the LCDN Operator or Content Provider to define which content will be ingested, cached, and delivered by an Aura LCDN.This API allows the CDN operator or content provider to manage the
  name: Akamai Aura LCDN Content Delivery API
  slug: akamai-aura-lcdn-content-delivery-api
- description: This API allows the Licensed CDN (LCDN) Operator to deploy and manage service instances for the LCDN product on the Aura platform.
  name: Akamai Aura LCDN Deployment API
  slug: akamai-aura-lcdn-deployment-api
- description: This API allows the Licensed CDN (LCDN) Operator to manage mapping configuration objects for the LCDN product on the Aura platform.
  name: Akamai Aura LCDN Mapping API
  slug: akamai-aura-lcdn-mapping-api
- description: This API allows the Licensed CDN (LCDN) Operator to manage LCDN service configuration on the Aura platform.
  name: Akamai Aura LCDN Services API
  slug: akamai-aura-lcdn-services-api
- description: The Aura Log Streaming API is applicable to all Aura delivery products. This API allows an LCDN or LMS operator to manage the streaming, or export, of transaction logs to external Kafka destinations i
  name: Akamai Aura Log Streaming API
  slug: akamai-aura-log-streaming-api
- description: This API allows the Aura Licensed CDN (LCDN) operator to programmatically block IP addresses associated with a specified IP CIDR block from accessing nodes on the LCDN for a pre-defined period of time
  name: Akamai Aura Network Policy API
  slug: akamai-aura-network-policy-api
- description: This API allows an LCDN operator to configure the AMC to communicate with an external secret store for storing TLS secrets. The API supports only secret stores based on Hashicorp-Vault. Hashicorp-Vaul
  name: Akamai Aura Secret Management API
  slug: akamai-aura-secret-management-api
- description: Manage support requests to resolve any issues with your Akamai applications and services using the Case Management API.
  name: Akamai Case Management API
  slug: akamai-case-management-api
- description: The Client Access Control (CAC) API helps you manage access between your web assets and the edge servers on the Akamai network. With this API you can retrieve information about the CIDR blocks that cu
  name: Akamai Client Access Control API
  slug: akamai-client-access-control-api
- description: The Cloud Access Manager (CAM) API connects the Akamai Intelligent Platform and your cloud provider. Use CAM to enable cloud origin authentication and securely store and manage your cloud provider ori
  name: Akamai Cloud Access Manager API
  slug: akamai-cloud-access-manager-api
- description: Use Cloud Wrapper to reduce origin requests by optimizing connectivity between cloud infrastructures and the Akamai Intelligent Edge.
  name: Akamai Cloud Wrapper Configuration API
  slug: akamai-cloud-wrapper-configuration-api
- description: Cloudlets are value-added applications that complement Akamais core delivery solutions to solve specific business challenges. Cloudlets bring a sites business logic closer to the end user by placing i
  name: Akamai Cloudlets API V3
  slug: akamai-cloudlets-api-v3
- description: You can use the CloudTest API service to plan for peak traffic performance by performance testing your environment safely and at scale to identify areas in your site or app that need strengthening. To
  name: Akamai CloudTest API
  slug: akamai-cloudtest-api
- description: The Contract API provides information about Akamai contracts and the products included in those contracts. With this API, you can retrieve product information for a specified time frame by contract ID
  name: Akamai Contract API
  slug: akamai-contract-api
- description: Now you can use the new version of the DataStream 2 API to capture log data and deliver them to a destination of your choice at low latency. We have redesigned the DataStream API for improved experien
  name: Akamai DataStream 2 API V2
  slug: akamai-datastream-2-api-v2
- description: Edge Diagnostics allows you to diagnose your server, DNS, and network problems from Akamai servers around the world.Once you extend your web content onto the Akamai edge network and apply various Akam
  name: Akamai Edge Diagnostics API
  slug: akamai-edge-diagnostics-api
- description: Welcome to Akamai Edge DNS service. Edge DNS integrates easily with your existing DNS infrastructure to provide a secure, high performance, highly available and scalable solution for DNS hosting. As p
  name: Akamai Edge DNS API V2
  slug: akamai-edge-dns-api-v2
- description: The Enhanced Content Control Utility (ECCU) is one of several supported Akamai purge interfaces. Use ECCU to specify the set of files to refresh on the edge network. Specify directories, file extensio
  name: Akamai Enhanced Content Control Utility (ECCU) API
  slug: akamai-enhanced-content-control-utility-eccu-api
- description: Enterprise Application Access allows you to integrate data path protection, single sign-on, identity access, application security, and management visibility and control for enterprise applications. EA
  name: Akamai Enterprise Application Access API
  slug: akamai-enterprise-application-access-api
- description: The Event Center API lets you access and manage event data available in Akamai Control Center for the contract type and account.This API offers a programmatic alternative to many of the features avail
  name: Akamai Event Center API
  slug: akamai-event-center-api
- description: Event Viewer records events completed through Control Center that are available to site administrators, such as configuration changes, login attempts, and log deliveries.With the Event Viewer API, you
  name: Akamai Event Viewer API
  slug: akamai-event-viewer-api
- description: Akamai periodically refreshes edge server IP addresses for routine maintenance. With Firewall Rules Notification, you can manage who receives email notifications about the planned changes. Akamai prov
  name: Akamai Firewall Rules Notification API
  slug: akamai-firewall-rules-notification-api
- description: The Internet domain name system (DNS) is a distributed system. It allows computer programs to issue queries about domain names which the DNS returns one or more answers to. The most common use for DNS
  name: Akamai Global Traffic Management API
  slug: akamai-global-traffic-management-api
- description: The Global Traffic Management Load Feedback API allows users to submit load data for a GTM domain in either JSON or XML format via POST, and to fetch the current load state via GET.
  name: Akamai Global Traffic Management Load Feedback API
  slug: akamai-global-traffic-management-load-feedback-api
- description: The Traffic Management Reporting API provides read-only reports on GTMs real time statistics. Each call allows you to view traffic, liveness, direct demand, load feedback, and latency on datacenters a
  name: Akamai Global Traffic Management Reporting API
  slug: akamai-global-traffic-management-reporting-api
- description: 'null'
  name: Akamai Identity and Access Management API V3
  slug: akamai-identity-and-access-management-api-v3
- description: The Authentication API provides methods for creating accounts on, and logging in to, websites and apps. Users can create these accounts, and log in, by using one of two approaches:.
  name: Akamai Identity Cloud Authentication API
  slug: akamai-identity-cloud-authentication-api
- description: The Configuration API is a large collection of endpoints revolving around three areas of Identity Cloud administration:.
  name: Akamai Identity Cloud Configuration API
  slug: akamai-identity-cloud-configuration-api
- description: Social login and registration enables users to register and login to your website by using an account created on a social login identity provider (IdP) such as Facebook or Twitter. For example, instea
  name: Akamai Identity Cloud Custom Provider API
  slug: akamai-identity-cloud-custom-provider-api
- description: 'Identity Cloud uses its own terminology when referring to user accounts and to the databases where user account information is stored. In Identity Cloud, the term entity is used when referencing user '
  name: Akamai Identity Cloud Entity and EntityType API
  slug: akamai-identity-cloud-entity-and-entitytype-api
- description: The Hosted Login, OAuth 2.0, and OpenID Connect APIs represent your primary toolset for managing Hosted Login. Most Hosted Login management tasks can only be carried out by using API calls. Keep in mi
  name: Akamai Identity Cloud Hosted Login API
  slug: akamai-identity-cloud-hosted-login-api
- description: Security Event and Information Management (SIEM) is a recognized standard for collecting, aggregating, and analyzing events that take place on a website or within an app. Identity Clouds SIEM event de
  name: Akamai Identity Cloud SIEM Event Service API
  slug: akamai-identity-cloud-siem-event-service-api
- description: The Social API manages and configures social login, the technology enabling users to create, and then log in to, an Identity Cloud website by using their Facebook account, their Twitter account, or an
  name: Akamai Identity Cloud Social API
  slug: akamai-identity-cloud-social-api
- description: Webhooks v3 sends you near real-time notifications any time a user account is created, deleted, or modified. Sometimes these notifications are invaluable in safeguarding your website. For example, a s
  name: Akamai Identity Cloud Webhooks V3 API
  slug: akamai-identity-cloud-webhooks-v3-api
- description: Image and Video Manager transforms a websites images by creating derivative images of various sizes and formats, and dynamically selecting the best image when requested by an end user.The API offers a
  name: Akamai Image and Video Manager API
  slug: akamai-image-and-video-manager-api
- description: The Invoicing API provides data about your Akamai invoices and credit memos.This API offers a programmatic alternative to the Your bills, Bills history, and Notifications features available in the Bil
  name: Akamai Invoicing API V4
  slug: akamai-invoicing-api-v4
- description: Ion is a suite of intelligent performance optimizations and controls that help to deliver superior website and iOS or Android app experiences. It combines the scalability of Akamais global content del
  name: Akamai Ion
  slug: akamai-ion
- description: Part of the Internet of Things (IoT) product, the OTA Updates module enables automotive companies to leverage the Akamai Intelligent Platform to provide a highly scalable, secure, and reliable mechani
  name: Akamai IoT OTA Updates API
  slug: akamai-iot-ota-updates-api
- description: The Token Access Control API allows you to programmatically create, manage, and store collections of public keys. It lets you upload public keys into key collections, activate key collections in the s
  name: Akamai IoT Token Access Control API
  slug: akamai-iot-token-access-control-api
- description: The Linode API lets you programmatically manage the full range of Akamai cloud computing products and services. Here are a few of the things you can do with this API:.
  name: Akamai Linode API
  slug: akamai-linode-api
- description: Media Services Live 4 lets you archive live streams in HLS and DASH formats for use as video on demand (VOD) content. You can use the Live Archive Management (LAM) API to do multiple things:.
  name: Akamai Live Archive Management API
  slug: akamai-live-archive-management-api
- description: Media Delivery Reports let you monitor and identify key trends of your Akamai delivery solutions, including Adaptive Media Delivery, Download Delivery, Object Delivery, and Akamai Cloud Embed (formerl
  name: Akamai Media Delivery Reports API
  slug: akamai-media-delivery-reports-api
- description: This API lets you monitor traffic for your Media Services Live 4 streams. These first-mile reports provide information on ingest quality, availability, and accelerated streams.
  name: Akamai Media Services Live Reports API
  slug: akamai-media-services-live-reports-api
- description: 'The Media Services Live (MSL) Stream Provisioning API lets you publish live streaming media content and retrieve it through the Akamai Intelligent Edge Platform or any content delivery network (CDN). '
  name: Akamai Media Services Live Stream Provisioning API
  slug: akamai-media-services-live-stream-provisioning-api
- description: You can use the mPulse API service to view real-time analytics and user measurement beacons for web sites to observe how real users interact within your sites.
  name: Akamai mPulse API
  slug: akamai-mpulse-api
- description: You can use Mutual TLS Edge Truststore API to create, manage, and activate certificate (CA) sets needed to set up mutual authentication (mTLS) sessions between a client and Akamai edge servers.Each CA
  name: Akamai Mutual TLS Edge Truststore API
  slug: akamai-mutual-tls-edge-truststore-api
- description: You can use the Mutual TLS Origin Keystore API to create, manage, and activate client certificates needed to set up mutual authentication (mTLS) sessions between the origin and Akamai edge servers.
  name: Akamai Mutual TLS Origin Keystore API
  slug: akamai-mutual-tls-origin-keystore-api
- description: NetStorage is a managed service that provides persistent, replicated storage of website content, including images, streaming media files, software, documents, and other digital objects. Content replic
  name: Akamai NetStorage Configuration API
  slug: akamai-netstorage-configuration-api
- description: This API provides various HTTP methods you can use to manage your NetStorage content. Communication uses the Edge network using a HTTP(S) client of your own design. The client could be a web-based bro
  name: Akamai NetStorage Usage API
  slug: akamai-netstorage-usage-api
- description: The Prolexic Analytics API exposes analytics data from Prolexic DDoS protection and monitoring services, such as IP Protect, which provides alerts and network bandwidth time-series data.
  name: Akamai Prolexic Analytics API
  slug: akamai-prolexic-analytics-api
- description: 'Prolexic IP Protect helps shield your site from DDoS attacks: attempts to disrupt your website by overwhelming it with Internet traffic. With IP Protect that isnt a problem, because most Internet traf'
  name: Akamai Prolexic IP Protect Configuration API
  slug: akamai-prolexic-ip-protect-configuration-api
- description: If youre using Akamai Intelligent Platform to deliver your content, you want to see how its performing. The Reporting API provides a wide range of reports, with new reports added periodically, and all
  name: Akamai Reporting API
  slug: akamai-reporting-api
- description: Use the Script Management API to create and view policies. These policies can help minimize performance impacts from third-party JavaScripts used by your site or app.
  name: Akamai Script Management API
  slug: akamai-script-management-api
- description: The Secure Internet Access Enterprise (SIA) Configuration API offers a programmatic interface to manage policy settings to protect against enterprise security and acceptable user policy related events
  name: Akamai Secure Internet Access Enterprise Configuration API V3
  slug: akamai-secure-internet-access-enterprise-configuration-api-v3
- description: The Secure Internet Access Enterprise (SIA) Reporting API lets you access and analyze reports for acceptable user policy (AUP) events, DNS activity, network traffic connections, security connector eve
  name: Akamai Secure Internet Access Enterprise Reporting API V3
  slug: akamai-secure-internet-access-enterprise-reporting-api-v3
- description: The service-level agreement (SLA) API provides programmatic access to SLA test configurations and the resulting reports.SLA tests measure certain availability and performance metrics. The results of t
  name: Akamai Service-Level Agreement API
  slug: akamai-service-level-agreement-api
- description: If youre an administrator who handles Akamai portal accounts and users, use this API to manage your IdP (identity provider) certificates. For details on how to manage all functions and information rel
  name: Akamai Single Sign-On Configuration API
  slug: akamai-single-sign-on-configuration-api
- description: Test Center allows you to test how configuration changes affect your web content on Akamai edge network. Prior to activation, you can check to make sure theyre not behaving in an unexpected manner. Th
  name: Akamai Test Center API
  slug: akamai-test-center-api
- description: The Access tokens API from Akamai — 2 operation(s) for access tokens.
  name: Akamai Access tokens API
  slug: akamai-access-tokens-api
- description: Get the activation history for a configuration.
  name: Akamai Activation history API
  slug: akamai-activation-history-api
- description: Get status information about your activations and activation requests.
  name: Akamai Activation status API
  slug: akamai-activation-status-api
- description: Manage your security configuration activations.
  name: Akamai Activations API
  slug: akamai-activations-api
- description: The Active property hostnames API from Akamai — 2 operation(s) for active property hostnames.
  name: Akamai Active property hostnames API
  slug: akamai-active-property-hostnames-api
- description: Get the list of API endpoints associated with a security policy.
  name: Akamai API endpoints API
  slug: akamai-api-endpoints-api
- description: The API privacy API from Akamai — 1 operation(s) for api privacy.
  name: Akamai API privacy API
  slug: akamai-api-privacy-api
- description: Manage API request limits and the actions to take when those limits are met.
  name: Akamai API request constraints API
  slug: akamai-api-request-constraints-api
- description: Manage the attack payload log settings for your security configurations.
  name: Akamai Attack payload logs API
  slug: akamai-attack-payload-logs-api
- description: List all hostnames for a given contract and group.
  name: Akamai Available hostnames API
  slug: akamai-available-hostnames-api
- description: The Behavioral DDoS profile actions API from Akamai — 2 operation(s) for behavioral ddos profile actions.
  name: Akamai Behavioral DDoS profile actions API
  slug: akamai-behavioral-ddos-profile-actions-api
- description: The Behavioral DDoS profiles API from Akamai — 2 operation(s) for behavioral ddos profiles.
  name: Akamai Behavioral DDoS profiles API
  slug: akamai-behavioral-ddos-profiles-api
- description: The Behavioral DDoS protection profiles API from Akamai — 1 operation(s) for behavioral ddos protection profiles.
  name: Akamai Behavioral DDoS protection profiles API
  slug: akamai-behavioral-ddos-protection-profiles-api
- description: The Build API from Akamai — 1 operation(s) for build.
  name: Akamai Build API
  slug: akamai-build-api
- description: The Bulk activations API from Akamai — 2 operation(s) for bulk activations.
  name: Akamai Bulk activations API
  slug: akamai-bulk-activations-api
- description: The Bulk patch API from Akamai — 2 operation(s) for bulk patch.
  name: Akamai Bulk patch API
  slug: akamai-bulk-patch-api
- description: The Bulk search API from Akamai — 3 operation(s) for bulk search.
  name: Akamai Bulk search API
  slug: akamai-bulk-search-api
- description: The Bulk versioning API from Akamai — 2 operation(s) for bulk versioning.
  name: Akamai Bulk versioning API
  slug: akamai-bulk-versioning-api
- description: Manage the bypass network lists used with your security policies.
  name: Akamai Bypass network lists API
  slug: akamai-bypass-network-lists-api
- description: The Cache API from Akamai — 1 operation(s) for cache.
  name: Akamai Cache API
  slug: akamai-cache-api
- description: Purge by cache tag.
  name: Akamai Cache tag API
  slug: akamai-cache-tag-api
- description: The Categories API from Akamai — 2 operation(s) for categories.
  name: Akamai Categories API
  slug: akamai-categories-api
- description: The Challenge actions API from Akamai — 3 operation(s) for challenge actions.
  name: Akamai Challenge actions API
  slug: akamai-challenge-actions-api
- description: The Changes API from Akamai — 5 operation(s) for changes.
  name: Akamai Changes API
  slug: akamai-changes-api
- description: Manage your client reputation profiles.
  name: Akamai Client reputation API
  slug: akamai-client-reputation-api
- description: The Client settings API from Akamai — 1 operation(s) for client settings.
  name: Akamai Client settings API
  slug: akamai-client-settings-api
- description: The Client-Side Protections & Compliance API from Akamai — 1 operation(s) for client-side protections & compliance.
  name: Akamai Client-Side Protections & Compliance API
  slug: akamai-client-side-protections-compliance-api
- description: Manage hostnames you're currently evaluating for a configuration version. If using Web Application Protector, manage hostnames currently in evaluation mode. This mode lets you to see how your configur
  name: 'Akamai Configuration: Evaluation hostnames API'
  slug: akamai-configuration-evaluation-hostnames-api
- description: The Configuration version diff API from Akamai — 1 operation(s) for configuration version diff.
  name: Akamai Configuration version diff API
  slug: akamai-configuration-version-diff-api
- description: Get comprehensive details about a security configuration version.
  name: Akamai Configuration version export API
  slug: akamai-configuration-version-export-api
- description: The Contracts and groups API from Akamai — 4 operation(s) for contracts and groups.
  name: Akamai Contracts and groups API
  slug: akamai-contracts-and-groups-api
- description: The Contracts API from Akamai — 1 operation(s) for contracts.
  name: Akamai Contracts API
  slug: akamai-contracts-api
- description: The Cookie Settings API from Akamai — 1 operation(s) for cookie settings.
  name: Akamai Cookie Settings API
  slug: akamai-cookie-settings-api
- description: The CORS API from Akamai — 1 operation(s) for cors.
  name: Akamai CORS API
  slug: akamai-cors-api
- description: Purge by content provider (CP) code.
  name: Akamai CP code API
  slug: akamai-cp-code-api
- description: The CP codes API from Akamai — 2 operation(s) for cp codes.
  name: Akamai CP codes API
  slug: akamai-cp-codes-api
- description: The Custom behaviors API from Akamai — 2 operation(s) for custom behaviors.
  name: Akamai Custom behaviors API
  slug: akamai-custom-behaviors-api
- description: The Custom overrides API from Akamai — 2 operation(s) for custom overrides.
  name: Akamai Custom overrides API
  slug: akamai-custom-overrides-api
- description: Manage the actions contained in your custom rules. Use custom rules to handle scenarios not covered by the included standard rules or to quickly patch new website vulnerabilities.
  name: Akamai Custom rule actions API
  slug: akamai-custom-rule-actions-api
- description: See which CVEs are covered by App & API Protector. The catalog contains only CVEs that the Akamai Threat Research team is aware of. App & API Protector can identify and block attacks related to the ac
  name: Akamai CVE Protections lookup API
  slug: akamai-cve-protections-lookup-api
- description: The Deactivations API from Akamai — 2 operation(s) for deactivations.
  name: Akamai Deactivations API
  slug: akamai-deactivations-api
- description: The Deployments API from Akamai — 4 operation(s) for deployments.
  name: Akamai Deployments API
  slug: akamai-deployments-api
- description: Get information about APIs discovered in your traffic that are new or not yet protected under API protections.
  name: Akamai Discovered APIs API
  slug: akamai-discovered-apis-api
- description: The Edge hostnames API from Akamai — 2 operation(s) for edge hostnames.
  name: Akamai Edge hostnames API
  slug: akamai-edge-hostnames-api
- description: The EdgeKV status API from Akamai — 1 operation(s) for edgekv status.
  name: Akamai EdgeKV status API
  slug: akamai-edgekv-status-api
- description: The EdgeWorker IDs API from Akamai — 4 operation(s) for edgeworker ids.
  name: Akamai EdgeWorker IDs API
  slug: akamai-edgeworker-ids-api
- description: The EdgeWorkers API from Akamai — 1 operation(s) for edgeworkers.
  name: Akamai EdgeWorkers API
  slug: akamai-edgeworkers-api
- description: The Elements API from Akamai — 1 operation(s) for elements.
  name: Akamai Elements API
  slug: akamai-elements-api
- description: The Endpoints API from Akamai — 10 operation(s) for endpoints.
  name: Akamai Endpoints API
  slug: akamai-endpoints-api
- description: The Enrollments API from Akamai — 4 operation(s) for enrollments.
  name: Akamai Enrollments API
  slug: akamai-enrollments-api
- description: The Error responses API from Akamai — 2 operation(s) for error responses.
  name: Akamai Error responses API
  slug: akamai-error-responses-api
- description: Manage the evasive path match for your security configurations.
  name: Akamai Evasive path match API
  slug: akamai-evasive-path-match-api
- description: View security event data generated on the Akamai platform in your SIEM application.
  name: Akamai Events API
  slug: akamai-events-api
- description: Get a list of the failover hostnames in a security configuration.
  name: Akamai Failover hostnames API
  slug: akamai-failover-hostnames-api
- description: Manage security configurations and their versions.
  name: Akamai General configuration settings API
  slug: akamai-general-configuration-settings-api
- description: Manage security policies and their versions.
  name: Akamai General policy settings API
  slug: akamai-general-policy-settings-api
- description: The GraphQL API from Akamai — 1 operation(s) for graphql.
  name: Akamai GraphQL API
  slug: akamai-graphql-api
- description: The Groups API from Akamai — 1 operation(s) for groups.
  name: Akamai Groups API
  slug: akamai-groups-api
- description: The GZIP API from Akamai — 1 operation(s) for gzip.
  name: Akamai GZIP API
  slug: akamai-gzip-api
- description: The Hostname buckets API from Akamai — 3 operation(s) for hostname buckets.
  name: Akamai Hostname buckets API
  slug: akamai-hostname-buckets-api
- description: Get the list of hostnames in an account with their current protections, activation statuses, and other summary information.
  name: Akamai Hostname coverage API
  slug: akamai-hostname-coverage-api
- description: Manage the hostnames in your configuration settings.
  name: Akamai Hostnames API
  slug: akamai-hostnames-api
- description: Manage the HTTP header log settings for security policies.
  name: Akamai HTTP header logs API
  slug: akamai-http-header-logs-api
- description: The Include activations API from Akamai — 2 operation(s) for include activations.
  name: Akamai Include activations API
  slug: akamai-include-activations-api
- description: The Include version rules API from Akamai — 1 operation(s) for include version rules.
  name: Akamai Include version rules API
  slug: akamai-include-version-rules-api
- description: The Include versions API from Akamai — 5 operation(s) for include versions.
  name: Akamai Include versions API
  slug: akamai-include-versions-api
- description: The Includes API from Akamai — 4 operation(s) for includes.
  name: Akamai Includes API
  slug: akamai-includes-api
- description: Manage which network lists are used in the IP/Geo Firewall settings. If you want to add or remove IP addresses from the network lists, use the Network Lists API.
  name: Akamai IP/Geo Firewall settings API
  slug: akamai-ip-geo-firewall-settings-api
- description: The Items API from Akamai — 2 operation(s) for items.
  name: Akamai Items API
  slug: akamai-items-api
- description: The JA4 Client TLS Fingerprint API from Akamai — 1 operation(s) for ja4 client tls fingerprint.
  name: Akamai JA4 Client TLS Fingerprint API
  slug: akamai-ja4-client-tls-fingerprint-api
- description: The JWT API from Akamai — 1 operation(s) for jwt.
  name: Akamai JWT API
  slug: akamai-jwt-api
- description: The Limits API from Akamai — 1 operation(s) for limits.
  name: Akamai Limits API
  slug: akamai-limits-api
- description: Manage the actions taken by your malware policies.
  name: Akamai Malware policy actions API
  slug: akamai-malware-policy-actions-api
- description: Manage your Site Shield maps.
  name: Akamai Maps API
  slug: akamai-maps-api
- description: Manage your match targets, which define which security policy applies to an API, hostname, or path.
  name: Akamai Match targets API
  slug: akamai-match-targets-api
- description: The Namespaces API from Akamai — 5 operation(s) for namespaces.
  name: Akamai Namespaces API
  slug: akamai-namespaces-api
- description: The Network lists API from Akamai — 4 operation(s) for network lists.
  name: Akamai Network lists API
  slug: akamai-network-lists-api
- description: Manage your onboardings' activations, and the activation history for each onboarding.
  name: 'Akamai Onboarding: Activations and status API'
  slug: akamai-onboarding-activations-and-status-api
- description: Manage onboardings and their settings.
  name: 'Akamai Onboarding: Creation and settings API'
  slug: akamai-onboarding-creation-and-settings-api
- description: Manage your post-activation validations and CNAME your hostnames to Akamai in order to go live.
  name: 'Akamai Onboarding: Post-activation validation API'
  slug: akamai-onboarding-post-activation-validation-api
- description: The Permission groups API from Akamai — 4 operation(s) for permission groups.
  name: Akamai Permission groups API
  slug: akamai-permission-groups-api
- description: The Personally identifiable information API from Akamai — 6 operation(s) for personally identifiable information.
  name: Akamai Personally identifiable information API
  slug: akamai-personally-identifiable-information-api
- description: Manage settings for Personally Identifiable Information (PII) learning. With this feature, the network discovers PII on your behalf.
  name: Akamai PII learning API
  slug: akamai-pii-learning-api
- description: Manage the Pragma header settings for your security policies.
  name: Akamai Pragma settings API
  slug: akamai-pragma-settings-api
- description: Manage your prefetch request protections. When enabled, your application firewall rules inspect internal requests, which are those between your origin and Akamai's servers, for the file types you spec
  name: Akamai Prefetch requests API
  slug: akamai-prefetch-requests-api
- description: The Products API from Akamai — 3 operation(s) for products.
  name: Akamai Products API
  slug: akamai-products-api
- description: The Properties API from Akamai — 6 operation(s) for properties.
  name: Akamai Properties API
  slug: akamai-properties-api
- description: The Property activations API from Akamai — 2 operation(s) for property activations.
  name: Akamai Property activations API
  slug: akamai-property-activations-api
- description: The Property hostnames API from Akamai — 3 operation(s) for property hostnames.
  name: Akamai Property hostnames API
  slug: akamai-property-hostnames-api
- description: The Property version hostnames API from Akamai — 1 operation(s) for property version hostnames.
  name: Akamai Property version hostnames API
  slug: akamai-property-version-hostnames-api
- description: The Property version includes API from Akamai — 1 operation(s) for property version includes.
  name: Akamai Property version includes API
  slug: akamai-property-version-includes-api
- description: The Property version rules API from Akamai — 1 operation(s) for property version rules.
  name: Akamai Property version rules API
  slug: akamai-property-version-rules-api
- description: The Property versions API from Akamai — 5 operation(s) for property versions.
  name: Akamai Property versions API
  slug: akamai-property-versions-api
- description: 'Manage various security policy protections. These settings enable or disable each protection on your policy. However, you set the protections themselves in their corresponding operations available in '
  name: Akamai Protections API
  slug: akamai-protections-api
- description: Groups operations that let you control rate limits.
  name: Akamai Rate limits API
  slug: akamai-rate-limits-api
- description: Manage rate policy actions, which are the actions each policy takes when conditions are met.
  name: Akamai Rate policy actions API
  slug: akamai-rate-policy-actions-api
- description: The Reporting groups API from Akamai — 2 operation(s) for reporting groups.
  name: Akamai Reporting groups API
  slug: akamai-reporting-groups-api
- description: The Reports API from Akamai — 2 operation(s) for reports.
  name: Akamai Reports API
  slug: akamai-reports-api
- description: If using Kona Site Defender, manage the reputation analysis settings.
  name: Akamai Reputation analysis API
  slug: akamai-reputation-analysis-api
- description: Manage limits for the maximum request body size allowed.
  name: Akamai Request body inspection limits API
  slug: akamai-request-body-inspection-limits-api
- description: Manage a security configuration's inspection limit settings for request bodies.
  name: Akamai Request body size API
  slug: akamai-request-body-size-api
- description: The Resource tiers API from Akamai — 1 operation(s) for resource tiers.
  name: Akamai Resource tiers API
  slug: akamai-resource-tiers-api
- description: The Resources API from Akamai — 3 operation(s) for resources.
  name: Akamai Resources API
  slug: akamai-resources-api
- description: The Revisions API from Akamai — 8 operation(s) for revisions.
  name: Akamai Revisions API
  slug: akamai-revisions-api
- description: The Rotate JWT API from Akamai — 1 operation(s) for rotate jwt.
  name: Akamai Rotate JWT API
  slug: akamai-rotate-jwt-api
- description: The Routing API from Akamai — 1 operation(s) for routing.
  name: Akamai Routing API
  slug: akamai-routing-api
- description: The Rule formats API from Akamai — 1 operation(s) for rule formats.
  name: Akamai Rule formats API
  slug: akamai-rule-formats-api
- description: The Sandboxes API from Akamai — 3 operation(s) for sandboxes.
  name: Akamai Sandboxes API
  slug: akamai-sandboxes-api
- description: The Schemas API from Akamai — 2 operation(s) for schemas.
  name: Akamai Schemas API
  slug: akamai-schemas-api
- description: The Search API from Akamai — 1 operation(s) for search.
  name: Akamai Search API
  slug: akamai-search-api
- description: The Secure tokens API from Akamai — 2 operation(s) for secure tokens.
  name: Akamai Secure tokens API
  slug: akamai-secure-tokens-api
- description: Manage the attack groups and rules that you're currently evaluating for your security policies.
  name: 'Akamai Security policy: Conditions and exceptions API'
  slug: akamai-security-policy-conditions-and-exceptions-api
- description: Manage the attack groups that you're evaluating for your security configurations and policies.
  name: 'Akamai Security policy: Evaluation attack groups API'
  slug: akamai-security-policy-evaluation-attack-groups-api
- description: Manage hostnames you're currently evaluating for security policies.
  name: 'Akamai Security policy: Evaluation hostnames API'
  slug: akamai-security-policy-evaluation-hostnames-api
- description: Set the evaluation mode for your security policies. This mode runs concurrently with your existing Web Application Firewall Rule settings and records how the rules would respond if applied to live tra
  name: 'Akamai Security policy: Evaluation mode API'
  slug: akamai-security-policy-evaluation-mode-api
- description: Manage the penalty box settings that you're evaluating for your security policies.
  name: 'Akamai Security policy: Evaluation penalty box API'
  slug: akamai-security-policy-evaluation-penalty-box-api
- description: Manage the rules you're currently evaluating for security policies.
  name: 'Akamai Security policy: Evaluation rules API'
  slug: akamai-security-policy-evaluation-rules-api
- description: Manage your custom deny actions for security configurations and policies. Custom deny actions let you serve error messages, pages, and responses that meet your organization's unique needs.
  name: 'Akamai Shared resources: Custom deny actions API'
  slug: akamai-shared-resources-custom-deny-actions-api
- description: Manage your custom rules for security configurations and policies.
  name: 'Akamai Shared resources: Custom rules API'
  slug: akamai-shared-resources-custom-rules-api
- description: Manage your malware policies.
  name: 'Akamai Shared resources: Malware policies API'
  slug: akamai-shared-resources-malware-policies-api
- description: Manage rate policies for security configurations.
  name: 'Akamai Shared resources: Rate policies API'
  slug: akamai-shared-resources-rate-policies-api
- description: Manage your reputation profiles. Reputation protections identify potentially malicious IP addresses, scoring them based on prior interactions with other Akamai customers.
  name: 'Akamai Shared resources: Reputation profiles API'
  slug: akamai-shared-resources-reputation-profiles-api
- description: Manage SIEM settings for your security configurations.
  name: Akamai SIEM settings API
  slug: akamai-siem-settings-api
- description: Manage your slow POST protection settings for your security policies.
  name: Akamai Slow POST protections API
  slug: akamai-slow-post-protections-api
- description: Manage the email subscriptions for features within a specific security configuration.
  name: Akamai Subscriptions API
  slug: akamai-subscriptions-api
- description: Purge by URL or by Akamai resource locator (ARL).
  name: Akamai URL/ARL API
  slug: akamai-url-arl-api
- description: Manage your URL protection policies.
  name: Akamai URL protection policies API
  slug: akamai-url-protection-policies-api
- description: Manage your URL protection settings for your security policies.
  name: Akamai URL protection policy actions API
  slug: akamai-url-protection-policy-actions-api
- description: The Validations API from Akamai — 1 operation(s) for validations.
  name: Akamai Validations API
  slug: akamai-validations-api
- description: The Versions API from Akamai — 11 operation(s) for versions.
  name: Akamai Versions API
  slug: akamai-versions-api
- description: Manage your WAF attack groups.
  name: 'Akamai WAF rules: Attack groups API'
  slug: akamai-waf-rules-attack-groups-api
- description: Manage the penalty box condition settings for your firewall rules.
  name: 'Akamai WAF rules: Evaluation Penalty box conditions API'
  slug: akamai-waf-rules-evaluation-penalty-box-conditions-api
- description: Manage your Web Application Firewall (WAF) rules and rule sets.
  name: 'Akamai WAF rules: General settings API'
  slug: akamai-waf-rules-general-settings-api
- description: Manage the penalty box settings for your Web Application Firewall implementation.
  name: 'Akamai WAF rules: Penalty box API'
  slug: akamai-waf-rules-penalty-box-api
- description: Manage the conditions used with your Web Application Firewall's penalty box.
  name: 'Akamai WAF rules: Penalty box conditions API'
  slug: akamai-waf-rules-penalty-box-conditions-api
- description: Quickly manage and mitigate risks resulting from the most recent high-profile, critical vulnerabilities. __Note__. Rapid rules are rules you can apply while we are still testing and perfecting them. O
  name: 'Akamai WAF rules: Rapid rules API'
  slug: akamai-waf-rules-rapid-rules-api
- description: Manage the tuning recommendations for your WAF attack groups.
  name: 'Akamai WAF rules: Tuning recommendations API'
  slug: akamai-waf-rules-tuning-recommendations-api
- description: Manage the mode used with your WAF rules. Your mode you set determines how your rule sets are updated.
  name: 'Akamai WAF rules: Update mode API'
  slug: akamai-waf-rules-update-mode-api
- description: The Watermark limits API from Akamai — 2 operation(s) for watermark limits.
  name: Akamai Watermark limits API
  slug: akamai-watermark-limits-api
artifact_total: 998
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens API'
  slug: open-akamai-access-tokens-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Activation history API'
  slug: open-akamai-activation-history-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Activation status API'
  slug: open-akamai-activation-status-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Activations API'
  slug: open-akamai-activations-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Active property hostnames API'
  slug: open-akamai-active-property-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition API'
  slug: open-akamai-api-definitions
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens API endpoints API'
  slug: open-akamai-api-endpoints-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens API privacy API'
  slug: open-akamai-api-privacy-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens API request constraints API'
  slug: open-akamai-api-request-constraints-api
- collection_type: open
  name: 'Akamai: Application Security API'
  slug: open-akamai-application-security
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Attack payload logs API'
  slug: open-akamai-attack-payload-logs-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Available hostnames API'
  slug: open-akamai-available-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Behavioral DDoS profile actions API'
  slug: open-akamai-behavioral-ddos-profile-actions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Behavioral DDoS profiles API'
  slug: open-akamai-behavioral-ddos-profiles-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Behavioral DDoS protection profiles API'
  slug: open-akamai-behavioral-ddos-protection-profiles-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Build API'
  slug: open-akamai-build-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Bulk activations API'
  slug: open-akamai-bulk-activations-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Bulk patch API'
  slug: open-akamai-bulk-patch-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Bulk search API'
  slug: open-akamai-bulk-search-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Bulk versioning API'
  slug: open-akamai-bulk-versioning-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Bypass network lists API'
  slug: open-akamai-bypass-network-lists-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Cache API'
  slug: open-akamai-cache-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Cache tag API'
  slug: open-akamai-cache-tag-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Categories API'
  slug: open-akamai-categories-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Challenge actions API'
  slug: open-akamai-challenge-actions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Changes API'
  slug: open-akamai-changes-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Client reputation API'
  slug: open-akamai-client-reputation-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Client settings API'
  slug: open-akamai-client-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Client-Side Protections & Compliance API'
  slug: open-akamai-client-side-protections-compliance-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Configuration: Evaluation hostnames API'
  slug: open-akamai-configuration-evaluation-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Configuration version diff API'
  slug: open-akamai-configuration-version-diff-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Configuration version export API'
  slug: open-akamai-configuration-version-export-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Contracts and groups API'
  slug: open-akamai-contracts-and-groups-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Contracts API'
  slug: open-akamai-contracts-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Cookie Settings API'
  slug: open-akamai-cookie-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens CORS API'
  slug: open-akamai-cors-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens CP code API'
  slug: open-akamai-cp-code-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens CP codes API'
  slug: open-akamai-cp-codes-api
- collection_type: open
  name: 'Akamai: CP Codes and Reporting Groups API'
  slug: open-akamai-cp-codes
- collection_type: open
  name: 'Akamai: Certificate Provisioning System API'
  slug: open-akamai-cps
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Custom behaviors API'
  slug: open-akamai-custom-behaviors-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Custom overrides API'
  slug: open-akamai-custom-overrides-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Custom rule actions API'
  slug: open-akamai-custom-rule-actions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens CVE Protections lookup API'
  slug: open-akamai-cve-protections-lookup-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Deactivations API'
  slug: open-akamai-deactivations-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Deployments API'
  slug: open-akamai-deployments-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Discovered APIs API'
  slug: open-akamai-discovered-apis-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Edge hostnames API'
  slug: open-akamai-edge-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens EdgeKV status API'
  slug: open-akamai-edgekv-status-api
- collection_type: open
  name: 'Akamai: EdgeKV API'
  slug: open-akamai-edgekv
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens EdgeWorker IDs API'
  slug: open-akamai-edgeworker-ids-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens EdgeWorkers API'
  slug: open-akamai-edgeworkers-api
- collection_type: open
  name: 'Akamai: EdgeWorkers API'
  slug: open-akamai-edgeworkers
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Elements API'
  slug: open-akamai-elements-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Endpoints API'
  slug: open-akamai-endpoints-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Enrollments API'
  slug: open-akamai-enrollments-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Error responses API'
  slug: open-akamai-error-responses-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Evasive path match API'
  slug: open-akamai-evasive-path-match-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Events API'
  slug: open-akamai-events-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Failover hostnames API'
  slug: open-akamai-failover-hostnames-api
- collection_type: open
  name: 'Akamai: Fast Purge API'
  slug: open-akamai-fast-purge
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens General configuration settings API'
  slug: open-akamai-general-configuration-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens General policy settings API'
  slug: open-akamai-general-policy-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens GraphQL API'
  slug: open-akamai-graphql-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Groups API'
  slug: open-akamai-groups-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens GZIP API'
  slug: open-akamai-gzip-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Hostname buckets API'
  slug: open-akamai-hostname-buckets-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Hostname coverage API'
  slug: open-akamai-hostname-coverage-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Hostnames API'
  slug: open-akamai-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens HTTP header logs API'
  slug: open-akamai-http-header-logs-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Include activations API'
  slug: open-akamai-include-activations-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Include version rules API'
  slug: open-akamai-include-version-rules-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Include versions API'
  slug: open-akamai-include-versions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Includes API'
  slug: open-akamai-includes-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens IP/Geo Firewall settings API'
  slug: open-akamai-ip-geo-firewall-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Items API'
  slug: open-akamai-items-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens JA4 Client TLS Fingerprint API'
  slug: open-akamai-ja4-client-tls-fingerprint-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens JWT API'
  slug: open-akamai-jwt-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Limits API'
  slug: open-akamai-limits-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Malware policy actions API'
  slug: open-akamai-malware-policy-actions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Maps API'
  slug: open-akamai-maps-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Match targets API'
  slug: open-akamai-match-targets-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Namespaces API'
  slug: open-akamai-namespaces-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Network lists API'
  slug: open-akamai-network-lists-api
- collection_type: open
  name: 'Akamai: Network Lists API'
  slug: open-akamai-network-lists
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Onboarding: Activations and status API'
  slug: open-akamai-onboarding-activations-and-status-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Onboarding: Creation and settings API'
  slug: open-akamai-onboarding-creation-and-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Onboarding: Post-activation validation API'
  slug: open-akamai-onboarding-post-activation-validation-api
- collection_type: open
  name: 'Akamai: Property Manager API'
  slug: open-akamai-papi
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Permission groups API'
  slug: open-akamai-permission-groups-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Personally identifiable information API'
  slug: open-akamai-personally-identifiable-information-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens PII learning API'
  slug: open-akamai-pii-learning-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Pragma settings API'
  slug: open-akamai-pragma-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Prefetch requests API'
  slug: open-akamai-prefetch-requests-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Products API'
  slug: open-akamai-products-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Properties API'
  slug: open-akamai-properties-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Property activations API'
  slug: open-akamai-property-activations-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Property hostnames API'
  slug: open-akamai-property-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Property version hostnames API'
  slug: open-akamai-property-version-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Property version includes API'
  slug: open-akamai-property-version-includes-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Property version rules API'
  slug: open-akamai-property-version-rules-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Property versions API'
  slug: open-akamai-property-versions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Protections API'
  slug: open-akamai-protections-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Rate limits API'
  slug: open-akamai-rate-limits-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Rate policy actions API'
  slug: open-akamai-rate-policy-actions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Reporting groups API'
  slug: open-akamai-reporting-groups-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Reports API'
  slug: open-akamai-reports-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Reputation analysis API'
  slug: open-akamai-reputation-analysis-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Request body inspection limits API'
  slug: open-akamai-request-body-inspection-limits-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Request body size API'
  slug: open-akamai-request-body-size-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Resource tiers API'
  slug: open-akamai-resource-tiers-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Resources API'
  slug: open-akamai-resources-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Revisions API'
  slug: open-akamai-revisions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Rotate JWT API'
  slug: open-akamai-rotate-jwt-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Routing API'
  slug: open-akamai-routing-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Rule formats API'
  slug: open-akamai-rule-formats-api
- collection_type: open
  name: 'Akamai: Sandbox API'
  slug: open-akamai-sandbox
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Sandboxes API'
  slug: open-akamai-sandboxes-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Schemas API'
  slug: open-akamai-schemas-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Search API'
  slug: open-akamai-search-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Secure tokens API'
  slug: open-akamai-secure-tokens-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Security policy: Conditions and exceptions API'
  slug: open-akamai-security-policy-conditions-and-exceptions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Security policy: Evaluation attack groups API'
  slug: open-akamai-security-policy-evaluation-attack-groups-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Security policy: Evaluation hostnames API'
  slug: open-akamai-security-policy-evaluation-hostnames-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Security policy: Evaluation mode API'
  slug: open-akamai-security-policy-evaluation-mode-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Security policy: Evaluation penalty box API'
  slug: open-akamai-security-policy-evaluation-penalty-box-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Security policy: Evaluation rules API'
  slug: open-akamai-security-policy-evaluation-rules-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Shared resources: Custom deny actions API'
  slug: open-akamai-shared-resources-custom-deny-actions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Shared resources: Custom rules API'
  slug: open-akamai-shared-resources-custom-rules-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Shared resources: Malware policies API'
  slug: open-akamai-shared-resources-malware-policies-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Shared resources: Rate policies API'
  slug: open-akamai-shared-resources-rate-policies-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Shared resources: Reputation profiles API'
  slug: open-akamai-shared-resources-reputation-profiles-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens SIEM settings API'
  slug: open-akamai-siem-settings-api
- collection_type: open
  name: 'Akamai: SIEM Integration API'
  slug: open-akamai-siem
- collection_type: open
  name: 'Akamai: Site Shield API'
  slug: open-akamai-site-shield
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Slow POST protections API'
  slug: open-akamai-slow-post-protections-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Subscriptions API'
  slug: open-akamai-subscriptions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens URL/ARL API'
  slug: open-akamai-url-arl-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens URL protection policies API'
  slug: open-akamai-url-protection-policies-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens URL protection policy actions API'
  slug: open-akamai-url-protection-policy-actions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Validations API'
  slug: open-akamai-validations-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Versions API'
  slug: open-akamai-versions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: Attack groups API'
  slug: open-akamai-waf-rules-attack-groups-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: Evaluation Penalty box conditions API'
  slug: open-akamai-waf-rules-evaluation-penalty-box-conditions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: General settings API'
  slug: open-akamai-waf-rules-general-settings-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: Penalty box API'
  slug: open-akamai-waf-rules-penalty-box-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: Penalty box conditions API'
  slug: open-akamai-waf-rules-penalty-box-conditions-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: Rapid rules API'
  slug: open-akamai-waf-rules-rapid-rules-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: Tuning recommendations API'
  slug: open-akamai-waf-rules-tuning-recommendations-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens WAF rules: Update mode API'
  slug: open-akamai-waf-rules-update-mode-api
- collection_type: open
  name: 'Akamai: API Endpoint Definition Access tokens Watermark limits API'
  slug: open-akamai-watermark-limits-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/akamai/akamai-apis/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/akamai/akamai-apis/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/akamai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/akamai-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/akamai-technologies
- group: company
  title: ''
  type: Website
  url: https://www.akamai.com/
- group: start
  title: ''
  type: Portal
  url: https://techdocs.akamai.com/home/page/apis
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.akamai.com/
- group: auth
  title: ''
  type: Authentication
  url: https://techdocs.akamai.com/developer/docs/set-up-authentication-credentials
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/akamai
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/akamai/akamai-apis
- group: company
  title: ''
  type: Blog
  url: https://www.akamai.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.akamai.com/support
- group: operate
  title: ''
  type: StatusPage
  url: https://www.akamaistatus.com/
created: '2025-01-08'
description: Akamai is a global content delivery network (CDN), cloud services, and cybersecurity company that helps organizations deliver fast, reliable, and secure digital experiences. Akamai's intelligent edge platform spans over 4,000 locations in 130+ countries, enabling customers to accelerate content delivery, protect against cyberattacks, and run cloud applications at the edge of the internet.
examples:
- key_count: 6
  name: Akamai Delete Activation Example
  slug: akamai-delete-activation-example
- key_count: 6
  name: Akamai Delete Behavioral Ddos Profile Example
  slug: akamai-delete-behavioral-ddos-profile-example
- key_count: 6
  name: Akamai Delete Category Example
  slug: akamai-delete-category-example
- key_count: 6
  name: Akamai Delete Challenge Action Example
  slug: akamai-delete-challenge-action-example
- key_count: 6
  name: Akamai Delete Config Custom Rule Example
  slug: akamai-delete-config-custom-rule-example
- key_count: 6
  name: Akamai Delete Config Example
  slug: akamai-delete-config-example
- key_count: 6
  name: Akamai Delete Custom Deny Example
  slug: akamai-delete-custom-deny-example
- key_count: 6
  name: Akamai Delete Enrollment Change Example
  slug: akamai-delete-enrollment-change-example
- key_count: 6
  name: Akamai Delete Enrollment Example
  slug: akamai-delete-enrollment-example
- key_count: 6
  name: Akamai Delete Include Activation Example
  slug: akamai-delete-include-activation-example
- key_count: 6
  name: Akamai Delete Include Example
  slug: akamai-delete-include-example
- key_count: 6
  name: Akamai Delete Item Example
  slug: akamai-delete-item-example
- key_count: 6
  name: Akamai Delete Malware Policy Example
  slug: akamai-delete-malware-policy-example
- key_count: 6
  name: Akamai Delete Match Target Example
  slug: akamai-delete-match-target-example
- key_count: 6
  name: Akamai Delete Network List Elements Example
  slug: akamai-delete-network-list-elements-example
- key_count: 6
  name: Akamai Delete Network List Example
  slug: akamai-delete-network-list-example
- key_count: 6
  name: Akamai Delete Onboarding Example
  slug: akamai-delete-onboarding-example
- key_count: 6
  name: Akamai Delete Policy Example
  slug: akamai-delete-policy-example
- key_count: 6
  name: Akamai Delete Property Activation Example
  slug: akamai-delete-property-activation-example
- key_count: 6
  name: Akamai Delete Property Example
  slug: akamai-delete-property-example
- key_count: 6
  name: Akamai Delete Property Hostname Activations Example
  slug: akamai-delete-property-hostname-activations-example
- key_count: 6
  name: Akamai Delete Rate Policy Example
  slug: akamai-delete-rate-policy-example
- key_count: 6
  name: Akamai Delete Reporting Group Example
  slug: akamai-delete-reporting-group-example
- key_count: 6
  name: Akamai Delete Reputation Profile Example
  slug: akamai-delete-reputation-profile-example
- key_count: 6
  name: Akamai Delete Token Example
  slug: akamai-delete-token-example
- key_count: 6
  name: Akamai Delete Url Protection Policy Example
  slug: akamai-delete-url-protection-policy-example
- key_count: 6
  name: Akamai Delete Version Number Example
  slug: akamai-delete-version-number-example
- key_count: 6
  name: Akamai Get Activation Example
  slug: akamai-get-activation-example
- key_count: 6
  name: Akamai Get Activation History Example
  slug: akamai-get-activation-history-example
- key_count: 6
  name: Akamai Get Activations Example
  slug: akamai-get-activations-example
- key_count: 6
  name: Akamai Get Activations Status Example
  slug: akamai-get-activations-status-example
- key_count: 6
  name: Akamai Get Advanced Settings Attack Payload Logging Example
  slug: akamai-get-advanced-settings-attack-payload-logging-example
- key_count: 6
  name: Akamai Get Advanced Settings Cookie Settings Example
  slug: akamai-get-advanced-settings-cookie-settings-example
- key_count: 6
  name: Akamai Get Advanced Settings Logging Example
  slug: akamai-get-advanced-settings-logging-example
- key_count: 6
  name: Akamai Get Advanced Settings Pii Learning Example
  slug: akamai-get-advanced-settings-pii-learning-example
- key_count: 6
  name: Akamai Get Advanced Settings Pragma Header Example
  slug: akamai-get-advanced-settings-pragma-header-example
- key_count: 6
  name: Akamai Get Advanced Settings Prefetch Example
  slug: akamai-get-advanced-settings-prefetch-example
- key_count: 6
  name: Akamai Get Advanced Settings Request Body Example
  slug: akamai-get-advanced-settings-request-body-example
- key_count: 6
  name: Akamai Get Api Details Example
  slug: akamai-get-api-details-example
- key_count: 6
  name: Akamai Get Api Endpoints Example
  slug: akamai-get-api-endpoints-example
- key_count: 6
  name: Akamai Get Api List Example
  slug: akamai-get-api-list-example
- key_count: 6
  name: Akamai Get Api Privacy Settings Example
  slug: akamai-get-api-privacy-settings-example
- key_count: 6
  name: Akamai Get Api Request Constraints Example
  slug: akamai-get-api-request-constraints-example
- key_count: 6
  name: Akamai Get Attack Group Condition Exception Example
  slug: akamai-get-attack-group-condition-exception-example
- key_count: 6
  name: Akamai Get Attack Group Example
  slug: akamai-get-attack-group-example
- key_count: 6
  name: Akamai Get Available Behaviors Example
  slug: akamai-get-available-behaviors-example
- key_count: 6
  name: Akamai Get Available Criteria Example
  slug: akamai-get-available-criteria-example
- key_count: 6
  name: Akamai Get Behavioral Ddos Actions Example
  slug: akamai-get-behavioral-ddos-actions-example
- key_count: 6
  name: Akamai Get Behavioral Ddos Profile Example
  slug: akamai-get-behavioral-ddos-profile-example
- key_count: 6
  name: Akamai Get Behavioral Ddos Profiles Example
  slug: akamai-get-behavioral-ddos-profiles-example
- key_count: 6
  name: Akamai Get Build Example
  slug: akamai-get-build-example
- key_count: 6
  name: Akamai Get Bulk Activation Example
  slug: akamai-get-bulk-activation-example
- key_count: 6
  name: Akamai Get Bulk Patch Example
  slug: akamai-get-bulk-patch-example
- key_count: 6
  name: Akamai Get Bulk Search Example
  slug: akamai-get-bulk-search-example
- key_count: 6
  name: Akamai Get Bulk Version Example
  slug: akamai-get-bulk-version-example
- key_count: 6
  name: Akamai Get Bypass Network Lists Example
  slug: akamai-get-bypass-network-lists-example
- key_count: 6
  name: Akamai Get Bypass Network Lists Per Policy Example
  slug: akamai-get-bypass-network-lists-per-policy-example
- key_count: 6
  name: Akamai Get Cache Settings Example
  slug: akamai-get-cache-settings-example
- key_count: 6
  name: Akamai Get Categories Example
  slug: akamai-get-categories-example
- key_count: 6
  name: Akamai Get Category Example
  slug: akamai-get-category-example
- key_count: 6
  name: Akamai Get Challenge Action Example
  slug: akamai-get-challenge-action-example
- key_count: 6
  name: Akamai Get Challenge Actions Example
  slug: akamai-get-challenge-actions-example
- key_count: 6
  name: Akamai Get Change Allowed Input Param Example
  slug: akamai-get-change-allowed-input-param-example
- key_count: 6
  name: Akamai Get Change Deployment Schedule Example
  slug: akamai-get-change-deployment-schedule-example
- key_count: 6
  name: Akamai Get Client Settings Example
  slug: akamai-get-client-settings-example
- key_count: 6
  name: Akamai Get Condition Exception Example
  slug: akamai-get-condition-exception-example
- key_count: 6
  name: Akamai Get Config Custom Rule Example
  slug: akamai-get-config-custom-rule-example
- key_count: 6
  name: Akamai Get Config Example
  slug: akamai-get-config-example
- key_count: 6
  name: Akamai Get Config Versions Example
  slug: akamai-get-config-versions-example
- key_count: 6
  name: Akamai Get Configs Custom Rules Example
  slug: akamai-get-configs-custom-rules-example
- key_count: 6
  name: Akamai Get Configs Example
  slug: akamai-get-configs-example
- key_count: 6
  name: Akamai Get Contract Group Hosts Acgs Example
  slug: akamai-get-contract-group-hosts-acgs-example
- key_count: 6
  name: Akamai Get Contract Group Hosts Example
  slug: akamai-get-contract-group-hosts-example
- key_count: 6
  name: Akamai Get Contracts Example
  slug: akamai-get-contracts-example
- key_count: 6
  name: Akamai Get Contracts Groups Example
  slug: akamai-get-contracts-groups-example
- key_count: 6
  name: Akamai Get Cors Settings Example
  slug: akamai-get-cors-settings-example
- key_count: 6
  name: Akamai Get Coverage Match Targets Example
  slug: akamai-get-coverage-match-targets-example
- key_count: 6
  name: Akamai Get Cpcode Example
  slug: akamai-get-cpcode-example
- key_count: 6
  name: Akamai Get Cpcodes Example
  slug: akamai-get-cpcodes-example
- key_count: 6
  name: Akamai Get Cpcodes Watermark Limits Example
  slug: akamai-get-cpcodes-watermark-limits-example
- key_count: 6
  name: Akamai Get Custom Behavior Example
  slug: akamai-get-custom-behavior-example
- key_count: 6
  name: Akamai Get Custom Behaviors Example
  slug: akamai-get-custom-behaviors-example
- key_count: 6
  name: Akamai Get Custom Deny Action Example
  slug: akamai-get-custom-deny-action-example
- key_count: 6
  name: Akamai Get Custom Deny Actions Example
  slug: akamai-get-custom-deny-actions-example
- key_count: 6
  name: Akamai Get Custom Override Example
  slug: akamai-get-custom-override-example
- key_count: 6
  name: Akamai Get Custom Overrides Example
  slug: akamai-get-custom-overrides-example
- key_count: 6
  name: Akamai Get Custom Rules Example
  slug: akamai-get-custom-rules-example
- key_count: 6
  name: Akamai Get Cve Example
  slug: akamai-get-cve-example
- key_count: 6
  name: Akamai Get Cves Example
  slug: akamai-get-cves-example
- key_count: 6
  name: Akamai Get Deactivation Example
  slug: akamai-get-deactivation-example
- key_count: 6
  name: Akamai Get Deactivations Example
  slug: akamai-get-deactivations-example
- key_count: 6
  name: Akamai Get Deployment Staging Example
  slug: akamai-get-deployment-staging-example
- key_count: 6
  name: Akamai Get Deployments Example
  slug: akamai-get-deployments-example
- key_count: 6
  name: Akamai Get Deployments Production Example
  slug: akamai-get-deployments-production-example
- key_count: 6
  name: Akamai Get Discovered Api Endpoints Example
  slug: akamai-get-discovered-api-endpoints-example
- key_count: 6
  name: Akamai Get Dv History Example
  slug: akamai-get-dv-history-example
- key_count: 6
  name: Akamai Get Edgehostname Example
  slug: akamai-get-edgehostname-example
- key_count: 6
  name: Akamai Get Edgehostnames Example
  slug: akamai-get-edgehostnames-example
- key_count: 6
  name: Akamai Get Endpoint Version Example
  slug: akamai-get-endpoint-version-example
- key_count: 6
  name: Akamai Get Endpoint Version Pii Settings Example
  slug: akamai-get-endpoint-version-pii-settings-example
- key_count: 6
  name: Akamai Get Endpoint Version Piis Example
  slug: akamai-get-endpoint-version-piis-example
- key_count: 6
  name: Akamai Get Endpoint Version Resource Example
  slug: akamai-get-endpoint-version-resource-example
- key_count: 6
  name: Akamai Get Endpoint Version Resources Example
  slug: akamai-get-endpoint-version-resources-example
- key_count: 6
  name: Akamai Get Endpoint Versions Example
  slug: akamai-get-endpoint-versions-example
- key_count: 6
  name: Akamai Get Endpoints Example
  slug: akamai-get-endpoints-example
- key_count: 6
  name: Akamai Get Enrollment Change Example
  slug: akamai-get-enrollment-change-example
- key_count: 6
  name: Akamai Get Enrollment Example
  slug: akamai-get-enrollment-example
- key_count: 6
  name: Akamai Get Enrollments Example
  slug: akamai-get-enrollments-example
- key_count: 6
  name: Akamai Get Error Response Setting Example
  slug: akamai-get-error-response-setting-example
- key_count: 6
  name: Akamai Get Error Responses Type Example
  slug: akamai-get-error-responses-type-example
- key_count: 6
  name: Akamai Get Eval Group Condition Exception Example
  slug: akamai-get-eval-group-condition-exception-example
- key_count: 6
  name: Akamai Get Eval Hostnames Example
  slug: akamai-get-eval-hostnames-example
- key_count: 6
  name: Akamai Get Eval Policy Penalty Box Conditions Example
  slug: akamai-get-eval-policy-penalty-box-conditions-example
- key_count: 6
  name: Akamai Get Eval Policy Penalty Box Example
  slug: akamai-get-eval-policy-penalty-box-example
- key_count: 6
  name: Akamai Get Evasive Path Match Example
  slug: akamai-get-evasive-path-match-example
- key_count: 6
  name: Akamai Get Evasive Path Match Per Config Example
  slug: akamai-get-evasive-path-match-per-config-example
- key_count: 6
  name: Akamai Get Export Config Version Async Result Example
  slug: akamai-get-export-config-version-async-result-example
- key_count: 6
  name: Akamai Get Export Config Version Async Task Status Example
  slug: akamai-get-export-config-version-async-task-status-example
- key_count: 6
  name: Akamai Get Export Config Version Example
  slug: akamai-get-export-config-version-example
- key_count: 6
  name: Akamai Get Failover Hostnames Example
  slug: akamai-get-failover-hostnames-example
- key_count: 6
  name: Akamai Get Graphql Settings Example
  slug: akamai-get-graphql-settings-example
- key_count: 6
  name: Akamai Get Group Example
  slug: akamai-get-group-example
- key_count: 6
  name: Akamai Get Group Items Example
  slug: akamai-get-group-items-example
- key_count: 6
  name: Akamai Get Groups Example
  slug: akamai-get-groups-example
- key_count: 6
  name: Akamai Get Gzip Settings Example
  slug: akamai-get-gzip-settings-example
- key_count: 6
  name: Akamai Get History Certificates Example
  slug: akamai-get-history-certificates-example
- key_count: 6
  name: Akamai Get History Changes Example
  slug: akamai-get-history-changes-example
- key_count: 6
  name: Akamai Get Hostname Audit History Example
  slug: akamai-get-hostname-audit-history-example
- key_count: 6
  name: Akamai Get Hostname Coverage Example
  slug: akamai-get-hostname-coverage-example
- key_count: 6
  name: Akamai Get Hostname Coverage Overlapping Example
  slug: akamai-get-hostname-coverage-overlapping-example
- key_count: 6
  name: Akamai Get Hostnames Example
  slug: akamai-get-hostnames-example
- key_count: 6
  name: Akamai Get Id Example
  slug: akamai-get-id-example
- key_count: 6
  name: Akamai Get Id Resource Tier Example
  slug: akamai-get-id-resource-tier-example
- key_count: 6
  name: Akamai Get Ids Example
  slug: akamai-get-ids-example
- key_count: 6
  name: Akamai Get Include Activation Example
  slug: akamai-get-include-activation-example
- key_count: 6
  name: Akamai Get Include Activations Example
  slug: akamai-get-include-activations-example
- key_count: 6
  name: Akamai Get Include Available Behaviors Example
  slug: akamai-get-include-available-behaviors-example
- key_count: 6
  name: Akamai Get Include Available Criteria Example
  slug: akamai-get-include-available-criteria-example
- key_count: 6
  name: Akamai Get Include Example
  slug: akamai-get-include-example
- key_count: 6
  name: Akamai Get Include Parents Example
  slug: akamai-get-include-parents-example
- key_count: 6
  name: Akamai Get Include Validation Example
  slug: akamai-get-include-validation-example
- key_count: 6
  name: Akamai Get Include Version Example
  slug: akamai-get-include-version-example
- key_count: 6
  name: Akamai Get Include Version Rules Example
  slug: akamai-get-include-version-rules-example
- key_count: 6
  name: Akamai Get Include Versions Example
  slug: akamai-get-include-versions-example
- key_count: 6
  name: Akamai Get Includes Example
  slug: akamai-get-includes-example
- key_count: 6
  name: Akamai Get Initialize Example
  slug: akamai-get-initialize-example
- key_count: 6
  name: Akamai Get Item Example
  slug: akamai-get-item-example
- key_count: 6
  name: Akamai Get Ja4 Fingerprint Settings Example
  slug: akamai-get-ja4-fingerprint-settings-example
- key_count: 6
  name: Akamai Get Jwt Settings Example
  slug: akamai-get-jwt-settings-example
- key_count: 6
  name: Akamai Get Latest Include Version Example
  slug: akamai-get-latest-include-version-example
- key_count: 6
  name: Akamai Get Latest Property Version Example
  slug: akamai-get-latest-property-version-example
- key_count: 6
  name: Akamai Get Limits Example
  slug: akamai-get-limits-example
- key_count: 6
  name: Akamai Get Malware Policies Actions Example
  slug: akamai-get-malware-policies-actions-example
- key_count: 6
  name: Akamai Get Malware Policies Example
  slug: akamai-get-malware-policies-example
- key_count: 6
  name: Akamai Get Malware Policy Content Types Example
  slug: akamai-get-malware-policy-content-types-example
- key_count: 6
  name: Akamai Get Malware Policy Example
  slug: akamai-get-malware-policy-example
- key_count: 6
  name: Akamai Get Map Example
  slug: akamai-get-map-example
- key_count: 6
  name: Akamai Get Maps Example
  slug: akamai-get-maps-example
- key_count: 6
  name: Akamai Get Match Target Example
  slug: akamai-get-match-target-example
- key_count: 6
  name: Akamai Get Match Targets Example
  slug: akamai-get-match-targets-example
- key_count: 6
  name: Akamai Get Namespace Example
  slug: akamai-get-namespace-example
- key_count: 6
  name: Akamai Get Namespace Groups Example
  slug: akamai-get-namespace-groups-example
- key_count: 6
  name: Akamai Get Namespaces Example
  slug: akamai-get-namespaces-example
- key_count: 6
  name: Akamai Get Network List Example
  slug: akamai-get-network-list-example
- key_count: 6
  name: Akamai Get Network List History Example
  slug: akamai-get-network-list-history-example
- key_count: 6
  name: Akamai Get Network List Status Example
  slug: akamai-get-network-list-status-example
- key_count: 6
  name: Akamai Get Network Lists Example
  slug: akamai-get-network-lists-example
- key_count: 6
  name: Akamai Get Onboarding Activation Status Example
  slug: akamai-get-onboarding-activation-status-example
- key_count: 6
  name: Akamai Get Onboarding Certificate Validation Example
  slug: akamai-get-onboarding-certificate-validation-example
- key_count: 6
  name: Akamai Get Onboarding Cname Records Example
  slug: akamai-get-onboarding-cname-records-example
- key_count: 6
  name: Akamai Get Onboarding Domain Validation Example
  slug: akamai-get-onboarding-domain-validation-example
- key_count: 6
  name: Akamai Get Onboarding Example
  slug: akamai-get-onboarding-example
- key_count: 6
  name: Akamai Get Onboarding Origin Validation Example
  slug: akamai-get-onboarding-origin-validation-example
- key_count: 6
  name: Akamai Get Onboarding Settings Example
  slug: akamai-get-onboarding-settings-example
- key_count: 6
  name: Akamai Get Onboardings Example
  slug: akamai-get-onboardings-example
- key_count: 6
  name: Akamai Get Policies Attack Payload Logging Example
  slug: akamai-get-policies-attack-payload-logging-example
- key_count: 6
  name: Akamai Get Policies Example
  slug: akamai-get-policies-example
- key_count: 6
  name: Akamai Get Policies Logging Example
  slug: akamai-get-policies-logging-example
- key_count: 6
  name: Akamai Get Policies Pragma Header Example
  slug: akamai-get-policies-pragma-header-example
- key_count: 6
  name: Akamai Get Policies Request Body Example
  slug: akamai-get-policies-request-body-example
- key_count: 6
  name: Akamai Get Policy Attack Group Example
  slug: akamai-get-policy-attack-group-example
- key_count: 6
  name: Akamai Get Policy Attack Groups Example
  slug: akamai-get-policy-attack-groups-example
- key_count: 6
  name: Akamai Get Policy Cpc Example
  slug: akamai-get-policy-cpc-example
- key_count: 6
  name: Akamai Get Policy Eval Group Example
  slug: akamai-get-policy-eval-group-example
- key_count: 6
  name: Akamai Get Policy Eval Groups Example
  slug: akamai-get-policy-eval-groups-example
- key_count: 6
  name: Akamai Get Policy Eval Rule Example
  slug: akamai-get-policy-eval-rule-example
- key_count: 6
  name: Akamai Get Policy Eval Rules Example
  slug: akamai-get-policy-eval-rules-example
- key_count: 6
  name: Akamai Get Policy Example
  slug: akamai-get-policy-example
- key_count: 6
  name: Akamai Get Policy Ip Geo Firewall Example
  slug: akamai-get-policy-ip-geo-firewall-example
- key_count: 6
  name: Akamai Get Policy Mode Example
  slug: akamai-get-policy-mode-example
- key_count: 6
  name: Akamai Get Policy Penalty Box Conditions Example
  slug: akamai-get-policy-penalty-box-conditions-example
- key_count: 6
  name: Akamai Get Policy Penalty Box Example
  slug: akamai-get-policy-penalty-box-example
- key_count: 6
  name: Akamai Get Policy Protections Example
  slug: akamai-get-policy-protections-example
- key_count: 6
  name: Akamai Get Policy Rapid Rule Action Example
  slug: akamai-get-policy-rapid-rule-action-example
- key_count: 6
  name: Akamai Get Policy Rapid Rule Condition Exception Example
  slug: akamai-get-policy-rapid-rule-condition-exception-example
- key_count: 6
  name: Akamai Get Policy Rapid Rule Lock Example
  slug: akamai-get-policy-rapid-rule-lock-example
- key_count: 6
  name: Akamai Get Policy Rapid Rules Action Example
  slug: akamai-get-policy-rapid-rules-action-example
- key_count: 6
  name: Akamai Get Policy Rapid Rules Example
  slug: akamai-get-policy-rapid-rules-example
- key_count: 6
  name: Akamai Get Policy Rapid Rules Status Example
  slug: akamai-get-policy-rapid-rules-status-example
- key_count: 6
  name: Akamai Get Policy Rules Example
  slug: akamai-get-policy-rules-example
- key_count: 6
  name: Akamai Get Policy Slow Post Example
  slug: akamai-get-policy-slow-post-example
- key_count: 6
  name: Akamai Get Product Mapping Use Cases Example
  slug: akamai-get-product-mapping-use-cases-example
- key_count: 6
  name: Akamai Get Products Example
  slug: akamai-get-products-example
- key_count: 6
  name: Akamai Get Properties Example
  slug: akamai-get-properties-example
- key_count: 6
  name: Akamai Get Property Activation Example
  slug: akamai-get-property-activation-example
- key_count: 6
  name: Akamai Get Property Activations Example
  slug: akamai-get-property-activations-example
- key_count: 6
  name: Akamai Get Property Example
  slug: akamai-get-property-example
- key_count: 6
  name: Akamai Get Property Hostname Activation Example
  slug: akamai-get-property-hostname-activation-example
- key_count: 6
  name: Akamai Get Property Hostname Activations Example
  slug: akamai-get-property-hostname-activations-example
- key_count: 6
  name: Akamai Get Property Hostnames Diff Example
  slug: akamai-get-property-hostnames-diff-example
- key_count: 6
  name: Akamai Get Property Hostnames Example
  slug: akamai-get-property-hostnames-example
- key_count: 6
  name: Akamai Get Property Version Example
  slug: akamai-get-property-version-example
- key_count: 6
  name: Akamai Get Property Version Hostnames Example
  slug: akamai-get-property-version-hostnames-example
- key_count: 6
  name: Akamai Get Property Version Includes Example
  slug: akamai-get-property-version-includes-example
- key_count: 6
  name: Akamai Get Property Version Rules Example
  slug: akamai-get-property-version-rules-example
- key_count: 6
  name: Akamai Get Property Versions Example
  slug: akamai-get-property-versions-example
- key_count: 6
  name: Akamai Get Rate Policies Actions Example
  slug: akamai-get-rate-policies-actions-example
- key_count: 6
  name: Akamai Get Rate Policies Example
  slug: akamai-get-rate-policies-example
- key_count: 6
  name: Akamai Get Rate Policy Example
  slug: akamai-get-rate-policy-example
- key_count: 6
  name: Akamai Get Recommendations Example
  slug: akamai-get-recommendations-example
- key_count: 6
  name: Akamai Get Recommendations Rule Example
  slug: akamai-get-recommendations-rule-example
- key_count: 6
  name: Akamai Get Report Example
  slug: akamai-get-report-example
- key_count: 6
  name: Akamai Get Reporting Group Example
  slug: akamai-get-reporting-group-example
- key_count: 6
  name: Akamai Get Reporting Group Products Example
  slug: akamai-get-reporting-group-products-example
- key_count: 6
  name: Akamai Get Reporting Groups Example
  slug: akamai-get-reporting-groups-example
- key_count: 6
  name: Akamai Get Reporting Groups Watermark Limits Example
  slug: akamai-get-reporting-groups-watermark-limits-example
- key_count: 6
  name: Akamai Get Reports Example
  slug: akamai-get-reports-example
- key_count: 6
  name: Akamai Get Reputation Analysis Example
  slug: akamai-get-reputation-analysis-example
- key_count: 6
  name: Akamai Get Reputation Profile Action Example
  slug: akamai-get-reputation-profile-action-example
- key_count: 6
  name: Akamai Get Reputation Profile Example
  slug: akamai-get-reputation-profile-example
- key_count: 6
  name: Akamai Get Reputation Profiles Actions Example
  slug: akamai-get-reputation-profiles-actions-example
- key_count: 6
  name: Akamai Get Reputation Profiles Example
  slug: akamai-get-reputation-profiles-example
- key_count: 6
  name: Akamai Get Resource Tiers Example
  slug: akamai-get-resource-tiers-example
- key_count: 6
  name: Akamai Get Revision Activations Example
  slug: akamai-get-revision-activations-example
- key_count: 6
  name: Akamai Get Revision Bom Example
  slug: akamai-get-revision-bom-example
- key_count: 6
  name: Akamai Get Revision Example
  slug: akamai-get-revision-example
- key_count: 6
  name: Akamai Get Revisions Example
  slug: akamai-get-revisions-example
- key_count: 6
  name: Akamai Get Routing Settings Example
  slug: akamai-get-routing-settings-example
- key_count: 6
  name: Akamai Get Rule Condition Exception Example
  slug: akamai-get-rule-condition-exception-example
- key_count: 6
  name: Akamai Get Rule Example
  slug: akamai-get-rule-example
- key_count: 6
  name: Akamai Get Rule Formats Example
  slug: akamai-get-rule-formats-example
- key_count: 6
  name: Akamai Get Rules Threat Intel Example
  slug: akamai-get-rules-threat-intel-example
- key_count: 6
  name: Akamai Get Rules Upgrade Details Example
  slug: akamai-get-rules-upgrade-details-example
- key_count: 6
  name: Akamai Get Sandbox Example
  slug: akamai-get-sandbox-example
- key_count: 6
  name: Akamai Get Sandbox Properties Example
  slug: akamai-get-sandbox-properties-example
- key_count: 6
  name: Akamai Get Sandbox Properties Rules Example
  slug: akamai-get-sandbox-properties-rules-example
- key_count: 6
  name: Akamai Get Sandbox Property Example
  slug: akamai-get-sandbox-property-example
- key_count: 6
  name: Akamai Get Sandboxes Example
  slug: akamai-get-sandboxes-example
- key_count: 6
  name: Akamai Get Schemas Product Rule Format Example
  slug: akamai-get-schemas-product-rule-format-example
- key_count: 6
  name: Akamai Get Schemas Request Filename Example
  slug: akamai-get-schemas-request-filename-example
- key_count: 6
  name: Akamai Get Secure Token Example
  slug: akamai-get-secure-token-example
- key_count: 6
  name: Akamai Get Security Coverage Example
  slug: akamai-get-security-coverage-example
- key_count: 6
  name: Akamai Get Selectable Hostnames Example
  slug: akamai-get-selectable-hostnames-example
- key_count: 6
  name: Akamai Get Selectable Hostnames Per Config Example
  slug: akamai-get-selectable-hostnames-per-config-example
- key_count: 6
  name: Akamai Get Selected Hostnames Eval Hostnames Example
  slug: akamai-get-selected-hostnames-eval-hostnames-example
- key_count: 6
  name: Akamai Get Selected Hostnames Example
  slug: akamai-get-selected-hostnames-example
- key_count: 6
  name: Akamai Get Selected Hostnames Per Policy Example
  slug: akamai-get-selected-hostnames-per-policy-example
- key_count: 6
  name: Akamai Get Siem Definitions Example
  slug: akamai-get-siem-definitions-example
- key_count: 6
  name: Akamai Get Siem Example
  slug: akamai-get-siem-example
- key_count: 6
  name: Akamai Get Subscribed Example
  slug: akamai-get-subscribed-example
- key_count: 6
  name: Akamai Get Subscription Feature Example
  slug: akamai-get-subscription-feature-example
- key_count: 6
  name: Akamai Get Token Example
  slug: akamai-get-token-example
- key_count: 6
  name: Akamai Get Tokens Example
  slug: akamai-get-tokens-example
- key_count: 6
  name: Akamai Get Url Protection Policies Actions Example
  slug: akamai-get-url-protection-policies-actions-example
- key_count: 6
  name: Akamai Get Url Protection Policies Example
  slug: akamai-get-url-protection-policies-example
- key_count: 6
  name: Akamai Get Url Protection Policy Example
  slug: akamai-get-url-protection-policy-example
- key_count: 6
  name: Akamai Get User Entitlements Example
  slug: akamai-get-user-entitlements-example
- key_count: 6
  name: Akamai Get Version Details Example
  slug: akamai-get-version-details-example
- key_count: 6
  name: Akamai Get Version Example
  slug: akamai-get-version-example
- key_count: 6
  name: Akamai Get Version Notes Example
  slug: akamai-get-version-notes-example
- key_count: 6
  name: Akamai Get Version Number Example
  slug: akamai-get-version-number-example
- key_count: 6
  name: Akamai Get Versions Example
  slug: akamai-get-versions-example
- key_count: 6
  name: Akamai Get Waf Policy Ruleset Composite Example
  slug: akamai-get-waf-policy-ruleset-composite-example
- key_count: 6
  name: Akamai Patch Endpoint Version Pii Status Example
  slug: akamai-patch-endpoint-version-pii-status-example
- key_count: 6
  name: Akamai Patch Include Version Rules Example
  slug: akamai-patch-include-version-rules-example
- key_count: 6
  name: Akamai Patch Property Hostnames Example
  slug: akamai-patch-property-hostnames-example
- key_count: 6
  name: Akamai Patch Property Version Hostnames Example
  slug: akamai-patch-property-version-hostnames-example
- key_count: 6
  name: Akamai Patch Property Version Rules Example
  slug: akamai-patch-property-version-rules-example
- key_count: 6
  name: Akamai Patch Waf Policy Ruleset Composite Example
  slug: akamai-patch-waf-policy-ruleset-composite-example
- key_count: 6
  name: Akamai Post Activations Example
  slug: akamai-post-activations-example
- key_count: 6
  name: Akamai Post Api Endpoint Resource Example
  slug: akamai-post-api-endpoint-resource-example
- key_count: 6
  name: Akamai Post Behavioral Ddos Profile Example
  slug: akamai-post-behavioral-ddos-profile-example
- key_count: 6
  name: Akamai Post Bulk Activations Example
  slug: akamai-post-bulk-activations-example
- key_count: 6
  name: Akamai Post Bulk Patch Example
  slug: akamai-post-bulk-patch-example
- key_count: 6
  name: Akamai Post Bulk Search Example
  slug: akamai-post-bulk-search-example
- key_count: 6
  name: Akamai Post Bulk Search Synch Example
  slug: akamai-post-bulk-search-synch-example
- key_count: 6
  name: Akamai Post Bulk Version Example
  slug: akamai-post-bulk-version-example
- key_count: 6
  name: Akamai Post Category Example
  slug: akamai-post-category-example
- key_count: 6
  name: Akamai Post Certificate Challenges Example
  slug: akamai-post-certificate-challenges-example
- key_count: 6
  name: Akamai Post Challenge Action Example
  slug: akamai-post-challenge-action-example
- key_count: 6
  name: Akamai Post Change Allowed Input Param Example
  slug: akamai-post-change-allowed-input-param-example
- key_count: 6
  name: Akamai Post Config Custom Rules Example
  slug: akamai-post-config-custom-rules-example
- key_count: 6
  name: Akamai Post Config Custom Rules Usage Example
  slug: akamai-post-config-custom-rules-usage-example
- key_count: 6
  name: Akamai Post Config Example
  slug: akamai-post-config-example
- key_count: 6
  name: Akamai Post Config Versions Diff Example
  slug: akamai-post-config-versions-diff-example
- key_count: 6
  name: Akamai Post Config Versions Example
  slug: akamai-post-config-versions-example
- key_count: 6
  name: Akamai Post Cpcodes Example
  slug: akamai-post-cpcodes-example
- key_count: 6
  name: Akamai Post Custom Deny Example
  slug: akamai-post-custom-deny-example
- key_count: 6
  name: Akamai Post Deactivations Example
  slug: akamai-post-deactivations-example
- key_count: 6
  name: Akamai Post Delete Cpcode Example
  slug: akamai-post-delete-cpcode-example
- key_count: 6
  name: Akamai Post Delete Tag Example
  slug: akamai-post-delete-tag-example
- key_count: 6
  name: Akamai Post Delete Url Example
  slug: akamai-post-delete-url-example
- key_count: 6
  name: Akamai Post Edgehostnames Example
  slug: akamai-post-edgehostnames-example
- key_count: 6
  name: Akamai Post Endpoint Clone Example
  slug: akamai-post-endpoint-clone-example
- key_count: 6
  name: Akamai Post Endpoint Hide Example
  slug: akamai-post-endpoint-hide-example
- key_count: 6
  name: Akamai Post Endpoint Show Example
  slug: akamai-post-endpoint-show-example
- key_count: 6
  name: Akamai Post Endpoint Version Activate Example
  slug: akamai-post-endpoint-version-activate-example
- key_count: 6
  name: Akamai Post Endpoint Version Clone Example
  slug: akamai-post-endpoint-version-clone-example
- key_count: 6
  name: Akamai Post Endpoint Version Deactivate Example
  slug: akamai-post-endpoint-version-deactivate-example
- key_count: 6
  name: Akamai Post Endpoint Version File Example
  slug: akamai-post-endpoint-version-file-example
- key_count: 6
  name: Akamai Post Endpoint Version Hide Example
  slug: akamai-post-endpoint-version-hide-example
- key_count: 6
  name: Akamai Post Endpoint Version Pii Settings Example
  slug: akamai-post-endpoint-version-pii-settings-example
- key_count: 6
  name: Akamai Post Endpoint Version Pii Status From Register Form Example
  slug: akamai-post-endpoint-version-pii-status-from-register-form-example
- key_count: 6
  name: Akamai Post Endpoint Version Piis Parameter Example
  slug: akamai-post-endpoint-version-piis-parameter-example
- key_count: 6
  name: Akamai Post Endpoints Example
  slug: akamai-post-endpoints-example
- key_count: 6
  name: Akamai Post Endpoints File Example
  slug: akamai-post-endpoints-file-example
- key_count: 6
  name: Akamai Post Endpoints Verify Secure Connection Example
  slug: akamai-post-endpoints-verify-secure-connection-example
- key_count: 6
  name: Akamai Post Enrollment Example
  slug: akamai-post-enrollment-example
- key_count: 6
  name: Akamai Post Export Config Version Async Task Example
  slug: akamai-post-export-config-version-async-task-example
- key_count: 6
  name: Akamai Post Id Clone Example
  slug: akamai-post-id-clone-example
- key_count: 6
  name: Akamai Post Ids Example
  slug: akamai-post-ids-example
- key_count: 6
  name: Akamai Post Include Activation Example
  slug: akamai-post-include-activation-example
- key_count: 6
  name: Akamai Post Include Versions Example
  slug: akamai-post-include-versions-example
- key_count: 6
  name: Akamai Post Includes Example
  slug: akamai-post-includes-example
- key_count: 6
  name: Akamai Post Invalidate Cpcode Example
  slug: akamai-post-invalidate-cpcode-example
- key_count: 6
  name: Akamai Post Invalidate Tag Example
  slug: akamai-post-invalidate-tag-example
- key_count: 6
  name: Akamai Post Invalidate Url Example
  slug: akamai-post-invalidate-url-example
- key_count: 6
  name: Akamai Post Malware Policies Example
  slug: akamai-post-malware-policies-example
- key_count: 6
  name: Akamai Post Map Acknowledge Example
  slug: akamai-post-map-acknowledge-example
- key_count: 6
  name: Akamai Post Match Targets Example
  slug: akamai-post-match-targets-example
- key_count: 6
  name: Akamai Post Namespace Example
  slug: akamai-post-namespace-example
- key_count: 6
  name: Akamai Post Network List Activate Example
  slug: akamai-post-network-list-activate-example
- key_count: 6
  name: Akamai Post Network List Append Example
  slug: akamai-post-network-list-append-example
- key_count: 6
  name: Akamai Post Network Lists Example
  slug: akamai-post-network-lists-example
- key_count: 6
  name: Akamai Post Notifications Subscribe Example
  slug: akamai-post-notifications-subscribe-example
- key_count: 6
  name: Akamai Post Notifications Unsubscribe Example
  slug: akamai-post-notifications-unsubscribe-example
- key_count: 6
  name: Akamai Post Onboarding Activation Example
  slug: akamai-post-onboarding-activation-example
- key_count: 6
  name: Akamai Post Onboarding Certificate Validation Example
  slug: akamai-post-onboarding-certificate-validation-example
- key_count: 6
  name: Akamai Post Onboarding Domain Validation Example
  slug: akamai-post-onboarding-domain-validation-example
- key_count: 6
  name: Akamai Post Onboarding Example
  slug: akamai-post-onboarding-example
- key_count: 6
  name: Akamai Post Onboarding Origin Validation Example
  slug: akamai-post-onboarding-origin-validation-example
- key_count: 6
  name: Akamai Post Policy Eval Example
  slug: akamai-post-policy-eval-example
- key_count: 6
  name: Akamai Post Policy Example
  slug: akamai-post-policy-example
- key_count: 6
  name: Akamai Post Properties Example
  slug: akamai-post-properties-example
- key_count: 6
  name: Akamai Post Property Activations Example
  slug: akamai-post-property-activations-example
- key_count: 6
  name: Akamai Post Property Versions Example
  slug: akamai-post-property-versions-example
- key_count: 6
  name: Akamai Post Rate Limit Status Example
  slug: akamai-post-rate-limit-status-example
- key_count: 6
  name: Akamai Post Rate Policies Example
  slug: akamai-post-rate-policies-example
- key_count: 6
  name: Akamai Post Recommendations Example
  slug: akamai-post-recommendations-example
- key_count: 6
  name: Akamai Post Reporting Groups Example
  slug: akamai-post-reporting-groups-example
- key_count: 6
  name: Akamai Post Reputation Profiles Example
  slug: akamai-post-reputation-profiles-example
- key_count: 6
  name: Akamai Post Resource Example
  slug: akamai-post-resource-example
- key_count: 6
  name: Akamai Post Revision Activations Example
  slug: akamai-post-revision-activations-example
- key_count: 6
  name: Akamai Post Revision Compare Example
  slug: akamai-post-revision-compare-example
- key_count: 6
  name: Akamai Post Revision Pin Example
  slug: akamai-post-revision-pin-example
- key_count: 6
  name: Akamai Post Revision Unpin Example
  slug: akamai-post-revision-unpin-example
- key_count: 6
  name: Akamai Post Rollback To Previous Active Version Example
  slug: akamai-post-rollback-to-previous-active-version-example
- key_count: 6
  name: Akamai Post Sandbox Clone Example
  slug: akamai-post-sandbox-clone-example
- key_count: 6
  name: Akamai Post Sandbox Example
  slug: akamai-post-sandbox-example
- key_count: 6
  name: Akamai Post Sandbox Properties Example
  slug: akamai-post-sandbox-properties-example
- key_count: 6
  name: Akamai Post Sandbox Rotate Jwt Example
  slug: akamai-post-sandbox-rotate-jwt-example
- key_count: 6
  name: Akamai Post Search Find By Value Example
  slug: akamai-post-search-find-by-value-example
- key_count: 6
  name: Akamai Post Secure Token Example
  slug: akamai-post-secure-token-example
- key_count: 6
  name: Akamai Post Skip Onboarding Origin Validation Example
  slug: akamai-post-skip-onboarding-origin-validation-example
- key_count: 6
  name: Akamai Post Subscribe Example
  slug: akamai-post-subscribe-example
- key_count: 6
  name: Akamai Post Subscription Feature Example
  slug: akamai-post-subscription-feature-example
- key_count: 6
  name: Akamai Post Tokens Example
  slug: akamai-post-tokens-example
- key_count: 6
  name: Akamai Post Unsubscribe Example
  slug: akamai-post-unsubscribe-example
- key_count: 6
  name: Akamai Post Url Protection Policies Example
  slug: akamai-post-url-protection-policies-example
- key_count: 6
  name: Akamai Post Validate Onboarding Cname Records Example
  slug: akamai-post-validate-onboarding-cname-records-example
- key_count: 6
  name: Akamai Post Validations Example
  slug: akamai-post-validations-example
- key_count: 6
  name: Akamai Post Version Show Example
  slug: akamai-post-version-show-example
- key_count: 6
  name: Akamai Post Versions Example
  slug: akamai-post-versions-example
- key_count: 6
  name: Akamai Put Advanced Settings Attack Payload Logging Example
  slug: akamai-put-advanced-settings-attack-payload-logging-example
- key_count: 6
  name: Akamai Put Advanced Settings Cookie Settings Example
  slug: akamai-put-advanced-settings-cookie-settings-example
- key_count: 6
  name: Akamai Put Advanced Settings Logging Example
  slug: akamai-put-advanced-settings-logging-example
- key_count: 6
  name: Akamai Put Advanced Settings Pii Learning Example
  slug: akamai-put-advanced-settings-pii-learning-example
- key_count: 6
  name: Akamai Put Advanced Settings Pragma Header Example
  slug: akamai-put-advanced-settings-pragma-header-example
- key_count: 6
  name: Akamai Put Advanced Settings Prefetch Example
  slug: akamai-put-advanced-settings-prefetch-example
- key_count: 6
  name: Akamai Put Advanced Settings Request Body Example
  slug: akamai-put-advanced-settings-request-body-example
- key_count: 6
  name: Akamai Put Api Privacy Settings Example
  slug: akamai-put-api-privacy-settings-example
- key_count: 6
  name: Akamai Put Api Request Constraints Api Example
  slug: akamai-put-api-request-constraints-api-example
- key_count: 6
  name: Akamai Put Api Request Constraints Example
  slug: akamai-put-api-request-constraints-example
- key_count: 6
  name: Akamai Put Api Visibility Example
  slug: akamai-put-api-visibility-example
- key_count: 6
  name: Akamai Put Attack Group Condition Exception Example
  slug: akamai-put-attack-group-condition-exception-example
- key_count: 6
  name: Akamai Put Attack Group Example
  slug: akamai-put-attack-group-example
- key_count: 6
  name: Akamai Put Auth Database Example
  slug: akamai-put-auth-database-example
- key_count: 6
  name: Akamai Put Behavioral Ddos Profile Action Example
  slug: akamai-put-behavioral-ddos-profile-action-example
- key_count: 6
  name: Akamai Put Behavioral Ddos Profile Example
  slug: akamai-put-behavioral-ddos-profile-example
- key_count: 6
  name: Akamai Put Bypass Network Lists Example
  slug: akamai-put-bypass-network-lists-example
- key_count: 6
  name: Akamai Put Bypass Network Lists Per Policy Example
  slug: akamai-put-bypass-network-lists-per-policy-example
- key_count: 6
  name: Akamai Put Cache Settings Example
  slug: akamai-put-cache-settings-example
- key_count: 6
  name: Akamai Put Category Example
  slug: akamai-put-category-example
- key_count: 6
  name: Akamai Put Challenge Action Example
  slug: akamai-put-challenge-action-example
- key_count: 6
  name: Akamai Put Change Deployment Schedule Example
  slug: akamai-put-change-deployment-schedule-example
- key_count: 6
  name: Akamai Put Client Settings Example
  slug: akamai-put-client-settings-example
- key_count: 6
  name: Akamai Put Condition Exception Example
  slug: akamai-put-condition-exception-example
- key_count: 6
  name: Akamai Put Config Custom Rule Example
  slug: akamai-put-config-custom-rule-example
- key_count: 6
  name: Akamai Put Config Example
  slug: akamai-put-config-example
- key_count: 6
  name: Akamai Put Cors Settings Example
  slug: akamai-put-cors-settings-example
- key_count: 6
  name: Akamai Put Cpcode Example
  slug: akamai-put-cpcode-example
- key_count: 6
  name: Akamai Put Custom Deny Example
  slug: akamai-put-custom-deny-example
- key_count: 6
  name: Akamai Put Custom Rule Example
  slug: akamai-put-custom-rule-example
- key_count: 6
  name: Akamai Put Endpoint Version Example
  slug: akamai-put-endpoint-version-example
- key_count: 6
  name: Akamai Put Enrollment Example
  slug: akamai-put-enrollment-example
- key_count: 6
  name: Akamai Put Error Response Setting Example
  slug: akamai-put-error-response-setting-example
- key_count: 6
  name: Akamai Put Eval Group Condition Exception Example
  slug: akamai-put-eval-group-condition-exception-example
- key_count: 6
  name: Akamai Put Eval Group Example
  slug: akamai-put-eval-group-example
- key_count: 6
  name: Akamai Put Eval Hostnames Example
  slug: akamai-put-eval-hostnames-example
- key_count: 6
  name: Akamai Put Eval Policy Penalty Box Conditions Example
  slug: akamai-put-eval-policy-penalty-box-conditions-example
- key_count: 6
  name: Akamai Put Eval Policy Penalty Box Example
  slug: akamai-put-eval-policy-penalty-box-example
- key_count: 6
  name: Akamai Put Evasive Path Match Example
  slug: akamai-put-evasive-path-match-example
- key_count: 6
  name: Akamai Put Evasive Path Match Per Config Example
  slug: akamai-put-evasive-path-match-per-config-example
- key_count: 6
  name: Akamai Put Get Error Responses Type Example
  slug: akamai-put-get-error-responses-type-example
- key_count: 6
  name: Akamai Put Google Recaptcha Secret Key Example
  slug: akamai-put-google-recaptcha-secret-key-example
- key_count: 6
  name: Akamai Put Graphql Settings Example
  slug: akamai-put-graphql-settings-example
- key_count: 6
  name: Akamai Put Gzip Settings Example
  slug: akamai-put-gzip-settings-example
- key_count: 6
  name: Akamai Put Id Example
  slug: akamai-put-id-example
- key_count: 6
  name: Akamai Put Include Version Rules Example
  slug: akamai-put-include-version-rules-example
- key_count: 6
  name: Akamai Put Initialize Example
  slug: akamai-put-initialize-example
- key_count: 6
  name: Akamai Put Item Example
  slug: akamai-put-item-example
- key_count: 6
  name: Akamai Put Ja4 Fingerprint Settings Example
  slug: akamai-put-ja4-fingerprint-settings-example
- key_count: 6
  name: Akamai Put Jwt Settings Example
  slug: akamai-put-jwt-settings-example
- key_count: 6
  name: Akamai Put Malware Policy Action Example
  slug: akamai-put-malware-policy-action-example
- key_count: 6
  name: Akamai Put Malware Policy Example
  slug: akamai-put-malware-policy-example
- key_count: 6
  name: Akamai Put Match Target Example
  slug: akamai-put-match-target-example
- key_count: 6
  name: Akamai Put Match Targets Sequence Example
  slug: akamai-put-match-targets-sequence-example
- key_count: 6
  name: Akamai Put Namespace Example
  slug: akamai-put-namespace-example
- key_count: 6
  name: Akamai Put Network List Details Example
  slug: akamai-put-network-list-details-example
- key_count: 6
  name: Akamai Put Network List Elements Example
  slug: akamai-put-network-list-elements-example
- key_count: 6
  name: Akamai Put Network List Example
  slug: akamai-put-network-list-example
- key_count: 6
  name: Akamai Put Onboarding Settings Example
  slug: akamai-put-onboarding-settings-example
- key_count: 6
  name: Akamai Put Policies Attack Payload Logging Example
  slug: akamai-put-policies-attack-payload-logging-example
- key_count: 6
  name: Akamai Put Policies Logging Example
  slug: akamai-put-policies-logging-example
- key_count: 6
  name: Akamai Put Policies Pragma Header Example
  slug: akamai-put-policies-pragma-header-example
- key_count: 6
  name: Akamai Put Policies Request Body Example
  slug: akamai-put-policies-request-body-example
- key_count: 6
  name: Akamai Put Policy Cpc Example
  slug: akamai-put-policy-cpc-example
- key_count: 6
  name: Akamai Put Policy Eval Rule Example
  slug: akamai-put-policy-eval-rule-example
- key_count: 6
  name: Akamai Put Policy Example
  slug: akamai-put-policy-example
- key_count: 6
  name: Akamai Put Policy Ip Geo Firewall Example
  slug: akamai-put-policy-ip-geo-firewall-example
- key_count: 6
  name: Akamai Put Policy Mode Example
  slug: akamai-put-policy-mode-example
- key_count: 6
  name: Akamai Put Policy Penalty Box Conditions Example
  slug: akamai-put-policy-penalty-box-conditions-example
- key_count: 6
  name: Akamai Put Policy Penalty Box Example
  slug: akamai-put-policy-penalty-box-example
- key_count: 6
  name: Akamai Put Policy Protections Example
  slug: akamai-put-policy-protections-example
- key_count: 6
  name: Akamai Put Policy Rapid Rule Action Example
  slug: akamai-put-policy-rapid-rule-action-example
- key_count: 6
  name: Akamai Put Policy Rapid Rule Condition Exception Example
  slug: akamai-put-policy-rapid-rule-condition-exception-example
- key_count: 6
  name: Akamai Put Policy Rapid Rule Lock Example
  slug: akamai-put-policy-rapid-rule-lock-example
- key_count: 6
  name: Akamai Put Policy Rapid Rules Action Example
  slug: akamai-put-policy-rapid-rules-action-example
- key_count: 6
  name: Akamai Put Policy Rapid Rules Status Example
  slug: akamai-put-policy-rapid-rules-status-example
- key_count: 6
  name: Akamai Put Policy Rules Example
  slug: akamai-put-policy-rules-example
- key_count: 6
  name: Akamai Put Policy Slow Post Example
  slug: akamai-put-policy-slow-post-example
- key_count: 6
  name: Akamai Put Property Version Hostnames Example
  slug: akamai-put-property-version-hostnames-example
- key_count: 6
  name: Akamai Put Property Version Rules Example
  slug: akamai-put-property-version-rules-example
- key_count: 6
  name: Akamai Put Protect Eval Hostnames Example
  slug: akamai-put-protect-eval-hostnames-example
- key_count: 6
  name: Akamai Put Protect Eval Hostnames Per Policy Example
  slug: akamai-put-protect-eval-hostnames-per-policy-example
- key_count: 6
  name: Akamai Put Rate Policy Action Example
  slug: akamai-put-rate-policy-action-example
- key_count: 6
  name: Akamai Put Rate Policy Evaluation Example
  slug: akamai-put-rate-policy-evaluation-example
- key_count: 6
  name: Akamai Put Rate Policy Example
  slug: akamai-put-rate-policy-example
- key_count: 6
  name: Akamai Put Reauthorize Namespace Example
  slug: akamai-put-reauthorize-namespace-example
- key_count: 6
  name: Akamai Put Reporting Group Example
  slug: akamai-put-reporting-group-example
- key_count: 6
  name: Akamai Put Reputation Analysis Example
  slug: akamai-put-reputation-analysis-example
- key_count: 6
  name: Akamai Put Reputation Profile Action Example
  slug: akamai-put-reputation-profile-action-example
- key_count: 6
  name: Akamai Put Reputation Profile Example
  slug: akamai-put-reputation-profile-example
- key_count: 6
  name: Akamai Put Routing Settings Example
  slug: akamai-put-routing-settings-example
- key_count: 6
  name: Akamai Put Rule Condition Exception Example
  slug: akamai-put-rule-condition-exception-example
- key_count: 6
  name: Akamai Put Rule Example
  slug: akamai-put-rule-example
- key_count: 6
  name: Akamai Put Rules Threat Intel Example
  slug: akamai-put-rules-threat-intel-example
- key_count: 6
  name: Akamai Put Sandbox Edgeworker Example
  slug: akamai-put-sandbox-edgeworker-example
- key_count: 6
  name: Akamai Put Sandbox Example
  slug: akamai-put-sandbox-example
- key_count: 6
  name: Akamai Put Sandbox Properties Rules Example
  slug: akamai-put-sandbox-properties-rules-example
- key_count: 6
  name: Akamai Put Sandbox Property Example
  slug: akamai-put-sandbox-property-example
- key_count: 6
  name: Akamai Put Selected Eval Hostnames Example
  slug: akamai-put-selected-eval-hostnames-example
- key_count: 6
  name: Akamai Put Selected Hostnames Example
  slug: akamai-put-selected-hostnames-example
- key_count: 6
  name: Akamai Put Selected Hostnames Per Config Example
  slug: akamai-put-selected-hostnames-per-config-example
- key_count: 6
  name: Akamai Put Siem Example
  slug: akamai-put-siem-example
- key_count: 6
  name: Akamai Put Url Protection Policy Action Example
  slug: akamai-put-url-protection-policy-action-example
- key_count: 6
  name: Akamai Put Url Protection Policy Example
  slug: akamai-put-url-protection-policy-example
- key_count: 6
  name: Akamai Put Version Notes Example
  slug: akamai-put-version-notes-example
- key_count: 6
  name: Akamai Put Version Resource Example
  slug: akamai-put-version-resource-example
features:
- 'Akamai (CDN + Cloud + Security): hundreds of services across CDN + Edge + Cloud'
- 'Detailed pricing: see https://www.akamai.com/products/pricing'
- 'Service: Akamai CDN'
- 'Service: Akamai Image & Video Manager'
- 'Service: Akamai Edge Workers (serverless)'
- 'Service: Akamai App & API Protector (WAF + DDoS + Bot)'
- 'Service: Akamai Cloud Computing (formerly Linode)'
- 'Service: Akamai Connected Cloud'
- 'Service: Akamai mPulse (RUM)'
- 'Service: Akamai DNS'
- 'Service: Akamai NetStorage'
finops:
- name: Akamai Finops
  service_category: CDN + Edge + Cloud
  slug: akamai-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/akamai.png
integrations:
- description: Official Akamai Terraform provider for infrastructure-as-code management of Akamai configurations.
  name: Terraform
- description: CI/CD integration for deploying Akamai configurations and properties via GitHub Actions.
  name: GitHub Actions
- description: DataStream and SIEM integration for streaming Akamai logs to Splunk for analysis.
  name: Splunk
- description: Cloud connectivity between Akamai edge and AWS origins for accelerated cloud delivery.
  name: AWS
json_schemas:
- name: attack-payload-logging-get-200
  property_count: 3
  slug: akamai-attack-payload-logging-get-200
- name: attack-payload-logging-put-200
  property_count: 3
  slug: akamai-attack-payload-logging-put-200
- name: attack-payload-logging-put
  property_count: 3
  slug: akamai-attack-payload-logging-put
- name: attack-payload-logging
  property_count: 1
  slug: akamai-attack-payload-logging
- name: NetworkListCondition
  property_count: 4
  slug: akamai-behavioral-ddos-bypass-client-list-condition
- name: RequestHeaderCondition
  property_count: 7
  slug: akamai-behavioral-ddos-bypass-request-header-condition
- name: behavioral-ddos-host-path-exception
  property_count: 2
  slug: akamai-behavioral-ddos-host-path-exception
- name: behavioral-ddos-profile
  property_count: 16
  slug: akamai-behavioral-ddos-profile
- name: behavioral-ddos-profiles
  property_count: 1
  slug: akamai-behavioral-ddos-profiles
- name: behavioral-ddos-sensitivity-override
  property_count: 3
  slug: akamai-behavioral-ddos-sensitivity-override
- name: behavioral-ddos-suspend
  property_count: 3
  slug: akamai-behavioral-ddos-suspend
- name: bypass-network-lists-get
  property_count: 1
  slug: akamai-bypass-network-lists-get
- name: bypass-network-lists-put
  property_count: 1
  slug: akamai-bypass-network-lists-put
- name: ClientReputationCondition
  property_count: 5
  slug: akamai-client-reputation-condition
- name: config-clone-post
  property_count: 2
  slug: akamai-config-clone-post
- name: config-custom-rules-usage-request
  property_count: 1
  slug: akamai-config-custom-rules-usage-request
- name: config-custom-rules-usage-response
  property_count: 1
  slug: akamai-config-custom-rules-usage-response
- name: config-get
  property_count: 7
  slug: akamai-config-get
- name: config-post
  property_count: 8
  slug: akamai-config-post
- name: config-rename
  property_count: 2
  slug: akamai-config-rename
- name: configs-get
  property_count: 1
  slug: akamai-configs-get
- name: cookie-settings
  property_count: 2
  slug: akamai-cookie-settings
- name: custom-denies
  property_count: 1
  slug: akamai-custom-denies
- name: custom-deny
  property_count: 4
  slug: akamai-custom-deny
- name: custom-rule
  property_count: 16
  slug: akamai-custom-rule
- name: custom-rules
  property_count: 1
  slug: akamai-custom-rules
- name: effectiveTimePeriod
  property_count: 3
  slug: akamai-effectivetimeperiod
- name: evasive-path-match-get-200
  property_count: 1
  slug: akamai-evasive-path-match-get-200
- name: evasive-path-match-put-200
  property_count: 1
  slug: akamai-evasive-path-match-put-200
- name: evasive-path-match-put
  property_count: 1
  slug: akamai-evasive-path-match-put
- name: header-logging-get-200
  property_count: 4
  slug: akamai-header-logging-get-200
- name: header-logging-put-200
  property_count: 4
  slug: akamai-header-logging-put-200
- name: header-logging-put
  property_count: 4
  slug: akamai-header-logging-put
- name: host-info-in-config
  property_count: 6
  slug: akamai-host-info-in-config
- name: hostname-coverage-match-target-get-200
  property_count: 1
  slug: akamai-hostname-coverage-match-target-get-200
- name: hostname-coverage-match-target
  property_count: 16
  slug: akamai-hostname-coverage-match-target
- name: hostname-coverage-overlapping-get-200
  property_count: 1
  slug: akamai-hostname-coverage-overlapping-get-200
- name: hostname-object
  property_count: 6
  slug: akamai-hostname-object
- name: hostnames
  property_count: 2
  slug: akamai-hostnames
- name: http-problem-details-nested
  property_count: 0
  slug: akamai-http-problem-details-nested
- name: http-problem-details
  property_count: 6
  slug: akamai-http-problem-details
- name: ja4-client-tls-fingerprint-get-200
  property_count: 1
  slug: akamai-ja4-client-tls-fingerprint-get-200
- name: ja4-client-tls-fingerprint-put-200
  property_count: 1
  slug: akamai-ja4-client-tls-fingerprint-put-200
- name: ja4-client-tls-fingerprint-put
  property_count: 1
  slug: akamai-ja4-client-tls-fingerprint-put
- name: logging-header-setting
  property_count: 2
  slug: akamai-logging-header-setting
- name: logging-option
  property_count: 3
  slug: akamai-logging-option
- name: malware-policies-content-types
  property_count: 1
  slug: akamai-malware-policies-content-types
- name: malware-policies
  property_count: 1
  slug: akamai-malware-policies
- name: malware-policy
  property_count: 9
  slug: akamai-malware-policy
- name: match-target
  property_count: 16
  slug: akamai-match-target
- name: match-targets
  property_count: 1
  slug: akamai-match-targets
- name: match-targets-sequence
  property_count: 2
  slug: akamai-match-targets-sequence
- name: overlap-config
  property_count: 6
  slug: akamai-overlap-config
- name: pii-learning
  property_count: 1
  slug: akamai-pii-learning
- name: post-cpcode
  property_count: 1
  slug: akamai-post-cpcode
- name: post-tag
  property_count: 1
  slug: akamai-post-tag
- name: post-url
  property_count: 1
  slug: akamai-post-url
- name: pragma-header
  property_count: 4
  slug: akamai-pragma-header
- name: prefetch-request-get-200
  property_count: 4
  slug: akamai-prefetch-request-get-200
- name: prefetch-request-put-200
  property_count: 4
  slug: akamai-prefetch-request-put-200
- name: prefetch-request-put
  property_count: 4
  slug: akamai-prefetch-request-put
- name: problem-details
  property_count: 6
  slug: akamai-problem-details
- name: problem-nested
  property_count: 0
  slug: akamai-problem-nested
- name: problem
  property_count: 6
  slug: akamai-problem
- name: rate-policies
  property_count: 1
  slug: akamai-rate-policies
- name: rate-policy-evaluation-put
  property_count: 1
  slug: akamai-rate-policy-evaluation-put
- name: rate-policy
  property_count: 30
  slug: akamai-rate-policy
- name: reputation-profile
  property_count: 9
  slug: akamai-reputation-profile
- name: reputation-profiles
  property_count: 1
  slug: akamai-reputation-profiles
- name: request-body
  property_count: 1
  slug: akamai-request-body
- name: RequestHeaderCondition
  property_count: 7
  slug: akamai-request-header-condition-2
- name: response
  property_count: 7
  slug: akamai-response
- name: security-controls
  property_count: 7
  slug: akamai-security-controls
- name: Event lines
  property_count: 11
  slug: akamai-siem-event-200
- name: Final metadata line
  property_count: 3
  slug: akamai-siem-response-context
- name: siem-settings
  property_count: 7
  slug: akamai-siem-settings
- name: siem-version
  property_count: 2
  slug: akamai-siem-version
- name: siem-versions
  property_count: 1
  slug: akamai-siem-versions
- name: site-shield-map
  property_count: 16
  slug: akamai-site-shield-map
- name: site-shield-maps
  property_count: 1
  slug: akamai-site-shield-maps
- name: streamed-response-200
  property_count: 0
  slug: akamai-streamed-response-200
- name: TlsFingerprintCondition
  property_count: 3
  slug: akamai-tls-fingerprint-condition
- name: NetworkListCondition
  property_count: 4
  slug: akamai-url-protection-bypass-client-list-condition
- name: RequestHeaderCondition
  property_count: 7
  slug: akamai-url-protection-bypass-request-header-condition
- name: urlProtectionCategory
  property_count: 1
  slug: akamai-url-protection-category
- name: urlProtectionCategory
  property_count: 3
  slug: akamai-url-protection-client-list-category
- name: url-protection-policies
  property_count: 1
  slug: akamai-url-protection-policies
- name: url-protection-policy-hostpath
  property_count: 2
  slug: akamai-url-protection-policy-hostpath
- name: url-protection-policy
  property_count: 18
  slug: akamai-url-protection-policy
- name: validation
  property_count: 5
  slug: akamai-validation
- name: validations
  property_count: 3
  slug: akamai-validations
- name: version-notes-get-200
  property_count: 1
  slug: akamai-version-notes-get-200
- name: version-notes-put-200
  property_count: 1
  slug: akamai-version-notes-put-200
- name: version-notes-put
  property_count: 1
  slug: akamai-version-notes-put
- name: waf-config-version
  property_count: 9
  slug: akamai-waf-config-version
- name: waf-config-versions
  property_count: 11
  slug: akamai-waf-config-versions
- name: attack-payload-logging-get-200
  property_count: 3
  slug: appsec-attack-payload-logging-get-200
- name: attack-payload-logging-put-200
  property_count: 3
  slug: appsec-attack-payload-logging-put-200
- name: attack-payload-logging-put
  property_count: 3
  slug: appsec-attack-payload-logging-put
- name: attack-payload-logging
  property_count: 1
  slug: appsec-attack-payload-logging
- name: NetworkListCondition
  property_count: 4
  slug: appsec-behavioral-ddos-bypass-client-list-condition
- name: RequestHeaderCondition
  property_count: 7
  slug: appsec-behavioral-ddos-bypass-request-header-condition
- name: behavioral-ddos-host-path-exception
  property_count: 2
  slug: appsec-behavioral-ddos-host-path-exception
- name: behavioral-ddos-profile
  property_count: 16
  slug: appsec-behavioral-ddos-profile
- name: behavioral-ddos-profiles
  property_count: 1
  slug: appsec-behavioral-ddos-profiles
- name: behavioral-ddos-sensitivity-override
  property_count: 3
  slug: appsec-behavioral-ddos-sensitivity-override
- name: behavioral-ddos-suspend
  property_count: 3
  slug: appsec-behavioral-ddos-suspend
- name: bypass-network-lists-get
  property_count: 1
  slug: appsec-bypass-network-lists-get
- name: bypass-network-lists-put
  property_count: 1
  slug: appsec-bypass-network-lists-put
- name: ClientReputationCondition
  property_count: 5
  slug: appsec-client-reputation-condition
- name: config-clone-post
  property_count: 2
  slug: appsec-config-clone-post
- name: config-custom-rules-usage-request
  property_count: 1
  slug: appsec-config-custom-rules-usage-request
- name: config-custom-rules-usage-response
  property_count: 1
  slug: appsec-config-custom-rules-usage-response
- name: config-get
  property_count: 7
  slug: appsec-config-get
- name: config-post
  property_count: 8
  slug: appsec-config-post
- name: config-rename
  property_count: 2
  slug: appsec-config-rename
- name: configs-get
  property_count: 1
  slug: appsec-configs-get
- name: cookie-settings
  property_count: 2
  slug: appsec-cookie-settings
- name: custom-denies
  property_count: 1
  slug: appsec-custom-denies
- name: custom-deny
  property_count: 4
  slug: appsec-custom-deny
- name: custom-rule
  property_count: 16
  slug: appsec-custom-rule
- name: post-cpcode
  property_count: 1
  slug: fast-purge-post-cpcode
- name: post-tag
  property_count: 1
  slug: fast-purge-post-tag
- name: post-url
  property_count: 1
  slug: fast-purge-post-url
- name: response
  property_count: 7
  slug: fast-purge-response
- name: problem-nested
  property_count: 0
  slug: siem-problem-nested
- name: problem
  property_count: 6
  slug: siem-problem
- name: Event lines
  property_count: 11
  slug: siem-siem-event-200
- name: Final metadata line
  property_count: 3
  slug: siem-siem-response-context
- name: streamed-response-200
  property_count: 0
  slug: siem-streamed-response-200
- name: http-problem-details-nested
  property_count: 0
  slug: site-shield-http-problem-details-nested
- name: http-problem-details
  property_count: 6
  slug: site-shield-http-problem-details
- name: site-shield-map
  property_count: 16
  slug: site-shield-site-shield-map
- name: site-shield-maps
  property_count: 1
  slug: site-shield-site-shield-maps
json_structures:
- name: Akamai Structure
  property_count: 0
  slug: akamai-structure
layout: provider
modified: '2026-05-30'
name: Akamai
nav: Providers
network: true
overview: 'Akamai publishes 141 APIs on the [APIs.io](https://apis.io/) network, including DataStream 2 API V2, Identity Cloud Webhooks V3 API, Access tokens API, and 138 more. Tagged areas include CDN, Cloud, Edge Computing, Networks, and Platform.


  The Akamai catalog on APIs.io includes 2 Spectral governance rulesets.


  Akamai''s developer surface includes developer portal, documentation, authentication, engineering blog, support, and 9 more developer resources.'
plans:
- name: Akamai Plans Pricing
  plan_count: 3
  slug: akamai-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 2
  name: Akamai Rate Limits
  slug: akamai-rate-limits
rules:
- name: Akamai API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: akamai-jsonschema-spectral-rules
- name: Akamai API Rules
  rule_count: 26
  severity_counts:
    error: 11
    hint: 0
    info: 5
    warn: 10
  slug: akamai-spectral-rules
score:
  band: developing
  composite: 42.5
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 64.3
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 42.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 139
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/screenshots/akamai-2026-06-20T171446.png
security:
- kind: domain-security
  name: Akamai Domain Security
  slug: akamai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: akamai
tags:
- CDN
- Cloud
- Edge Computing
- Networks
- Platform
- Security
use_cases:
- description: Broadcasters and OTT platforms deliver live and on-demand video at scale using Akamai Media Services.
  name: Media Streaming
- description: Retailers accelerate page load times and checkout flows with Ion and adaptive acceleration.
  name: E-Commerce Acceleration
- description: Enterprises implement zero trust access for applications using Enterprise Application Access.
  name: Zero Trust Security
- description: Organizations discover and protect APIs from threats using Akamai API Security platform.
  name: API Security
- description: Game publishers distribute updates, reduce latency, and prevent DDoS attacks on gaming platforms.
  name: Gaming
- description: Automotive and device manufacturers deliver secure over-the-air firmware updates via IoT OTA.
  name: IoT Firmware Updates
website: https://www.akamai.com/
---
