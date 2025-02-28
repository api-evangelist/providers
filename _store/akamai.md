---
aid: akamai
url: >-
  https://raw.githubusercontent.com/api-evangelist/akamai/refs/heads/main/apis.yml
apis:
  - aid: akamai:akamai-access-revocation-api
    name: Akamai Access Revocation API
    tags: []
    humanURL: https://techdocs.akamai.com/adaptive-media-delivery/reference/api
    properties:
      - url: https://techdocs.akamai.com/adaptive-media-delivery/reference/api
        type: Documentation
    description: >-
      Adaptive Media Delivery supports Token Authentication. You can apply it to
      generate unique tokens and include them in requests for your content.
      Akamai validates these tokens to grant access to your media. Access
      Revocation lets you recognize tokens that have been hijacked and flag them
      to block requests that include them. Use the Access Revocation API to
      generate a revocation list of these tokens. You can also set a time to
      live for this revocation period to automatically unrevoke these tokens, or
      you can manually remove them from a revocation list. The API also lets you
      review your revocation lists and Access Revocation settings.
  - aid: akamai:akamai-adaptive-acceleration-api
    name: Akamai Adaptive Acceleration API
    tags: []
    humanURL: https://techdocs.akamai.com/adaptive-acceleration/reference/api
    properties:
      - url: https://techdocs.akamai.com/adaptive-acceleration/reference/api
        type: Documentation
    description: >-
      The Adaptive Acceleration service takes advantage of the Server Push
      feature thats available with the HTTP/2 protocol, and Automatic Preconnect
      to increase page load speed.
  - aid: akamai:akamai-access-revocation-api
    name: Akamai Access Revocation API
    tags: []
    humanURL: https://techdocs.akamai.com/adaptive-media-delivery/reference/api
    properties:
      - url: https://techdocs.akamai.com/adaptive-media-delivery/reference/api
        type: Documentation
    description: >-
      Adaptive Media Delivery supports Token Authentication. You can apply it to
      generate unique tokens and include them in requests for your content.
      Akamai validates these tokens to grant access to your media. Access
      Revocation lets you recognize tokens that have been hijacked and flag them
      to block requests that include them. Use the Access Revocation API to
      generate a revocation list of these tokens. You can also set a time to
      live for this revocation period to automatically unrevoke these tokens, or
      you can manually remove them from a revocation list. The API also lets you
      review your revocation lists and Access Revocation settings.
  - aid: akamai:akamai-mfa-api
    name: Akamai MFA API
    tags: []
    humanURL: https://techdocs.akamai.com/mfa/reference/api
    properties:
      - url: https://techdocs.akamai.com/mfa/reference/api
        type: Documentation
    description: >-
      Akamai MFA provides strong secondary authentication to cloud, on-premises,
      web-based, SaaS, and IaaS applicationsin addition to your primary
      verification mechanism, like the identity provider (IdP) system.With this
      additional layer of protection, Akamai MFA increases the security of
      employee accounts and improves your zero-trust security posture.
  - aid: akamai:akamai-alerts-api
    name: Akamai Alerts API
    tags: []
    humanURL: https://techdocs.akamai.com/alerts-app/reference/api
    properties:
      - url: https://techdocs.akamai.com/alerts-app/reference/api
        type: Documentation
    description: >-
      The Alerts API allows you to configure notifications about significant
      changes to your traffic based on continual tracking by Akamais network
      monitoring platform. It allows you to create and modify alerts based on a
      wide range of criteria, both static and dynamic, and to configure reports
      on anomalies. This API provides you with a programmatic interface to the
      same functionality available in Akamai Control Center.
  - aid: akamai:akamai-api-endpoint-definition-api
    name: Akamai API Endpoint Definition API
    tags: []
    humanURL: https://techdocs.akamai.com/api-definitions/reference/api
    properties:
      - url: https://techdocs.akamai.com/api-definitions/reference/api
        type: Documentation
    description: >-
      The API Endpoint Definition API allows you to programmatically define an
      API endpoint and its set of component resources. If youre a Kona Site
      Defender customer, you can define request body and resource constraints
      and enforce them separately as allow lists in your Akamai web application
      firewall policy.
  - aid: akamai:akamai-api-keys-and-traffic-management-api
    name: Akamai API Keys and Traffic Management API
    tags: []
    humanURL: >-
      https://techdocs.akamai.com/key-traffic-mgmt/reference/api-keys-and-traffic-management-api
    properties:
      - url: >-
          https://techdocs.akamai.com/key-traffic-mgmt/reference/api-keys-and-traffic-management-api
        type: Documentation
    description: >-
      Like API Keys and Traffic Management in Akamai Control Center, this API
      lets you create and manage API keys that serve as unique identifiers for
      API consumers. API keys exist inside top-level units called key
      collections. At the key collection level, you can set a quota limit for
      the number of successful requests that individual API clients can make.
      You can also edit access control lists (ACLs) associated with your API
      endpoints and resources. Together with the API Endpoint Definition API,
      you can use this API to programmatically deploy your APIs on the Akamai
      network.
  - aid: akamai:akamai-application-security-api
    name: Akamai Application Security API
    tags: []
    humanURL: https://techdocs.akamai.com/application-security/reference/api
    properties:
      - url: https://techdocs.akamai.com/application-security/reference/api
        type: Documentation
    description: >-
      The Application Security API allows you to access and modify your Security
      Configurations for Kona Site Defender, Web Application Protector, App 
  - aid: akamai:akamai-aura-infrastructure-api
    name: Akamai Aura Infrastructure API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-infrastructure/reference/api
    properties:
      - url: https://techdocs.akamai.com/aura-infrastructure/reference/api
        type: Documentation
    description: >-
      This API allows the Licensed CDN (LCDN) Operator to create sites, nodes,
      and attribute types for LCDN or LMS products on the Aura platform. This
      API does not support the deployment of individual product components on
      the sites and nodes.
  - aid: akamai:akamai-aura-lcdn-content-control-api
    name: Akamai Aura LCDN Content Control API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-lcdn-content-control/reference/api
    properties:
      - url: https://techdocs.akamai.com/aura-lcdn-content-control/reference/api
        type: Documentation
    description: >-
      This API allows the LCDN Operator or Content Provider to purge content on
      the Aura LCDN. Purging removes outdated or unwanted content. Content can
      be purged one asset at a time, as a list of assets, or all assetswithin a
      directory using a wildcard. After an asset is purged, the first subsequent
      client request for the purged content results in a cache miss, and LCDN
      fetches a fresh copy from the origin server.
  - aid: akamai:akamai-aura-lcdn-content-delivery-api
    name: Akamai Aura LCDN Content Delivery API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-lcdn-content-delivery/reference/api
    properties:
      - url: https://techdocs.akamai.com/aura-lcdn-content-delivery/reference/api
        type: Documentation
    description: >-
      This API allows the LCDN Operator or Content Provider to define which
      content will be ingested, cached, and delivered by an Aura LCDN.This API
      allows the CDN operator or content provider to manage their own content
      delivery options, including origin servers, CDN prefixes, URI Filters and
      TLS Profiles.
  - aid: akamai:akamai-aura-lcdn-deployment-api
    name: Akamai Aura LCDN Deployment API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-lcdn-deployment/reference/overview
    properties:
      - url: https://techdocs.akamai.com/aura-lcdn-deployment/reference/overview
        type: Documentation
    description: >-
      This API allows the Licensed CDN (LCDN) Operator to deploy and manage
      service instances for the LCDN product on the Aura platform.
  - aid: akamai:akamai-aura-lcdn-mapping-api
    name: Akamai Aura LCDN Mapping API
    tags: []
    humanURL: >-
      https://techdocs.akamai.com/aura-lcdn-mapping/reference/aura-lcdn-mapping-api
    properties:
      - url: >-
          https://techdocs.akamai.com/aura-lcdn-mapping/reference/aura-lcdn-mapping-api
        type: Documentation
    description: >-
      This API allows the Licensed CDN (LCDN) Operator to manage mapping
      configuration objects for the LCDN product on the Aura platform.
  - aid: akamai:akamai-aura-lcdn-services-api
    name: Akamai Aura LCDN Services API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-lcdn-services/reference/api
    properties:
      - url: https://techdocs.akamai.com/aura-lcdn-services/reference/api
        type: Documentation
    description: >-
      This API allows the Licensed CDN (LCDN) Operator to manage LCDN service
      configuration on the Aura platform.
  - aid: akamai:akamai-aura-log-streaming-api
    name: Akamai Aura Log Streaming API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-log-streaming/reference/api
    properties:
      - url: https://techdocs.akamai.com/aura-log-streaming/reference/api
        type: Documentation
    description: >-
      The Aura Log Streaming API is applicable to all Aura delivery products.
      This API allows an LCDN or LMS operator to manage the streaming, or
      export, of transaction logs to external Kafka destinations in near
      real-time.
  - aid: akamai:akamai-aura-network-policy-api
    name: Akamai Aura Network Policy API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-network-policy/reference/api
    properties:
      - url: https://techdocs.akamai.com/aura-network-policy/reference/api
        type: Documentation
    description: >-
      This API allows the Aura Licensed CDN (LCDN) operator to programmatically
      block IP addresses associated with a specified IP CIDR block from
      accessing nodes on the LCDN for a pre-defined period of time. After the
      time expires, the IP addresses associated with the IP CIDR block will be
      unblocked.
  - aid: akamai:akamai-aura-secret-management-api
    name: Akamai Aura Secret Management API
    tags: []
    humanURL: https://techdocs.akamai.com/aura-secret-mgmt/reference/api
    properties:
      - url: https://techdocs.akamai.com/aura-secret-mgmt/reference/api
        type: Documentation
    description: >-
      This API allows an LCDN operator to configure the AMC to communicate with
      an external secret store for storing TLS secrets. The API supports only
      secret stores based on Hashicorp-Vault. Hashicorp-Vault is an open source
      secret management solution that secures, stores, and controls access to
      tokens, passwords, certificates, API keys and other secrets. For more
      information about Hashicorp-Vault, see the Hashicorp site.
  - aid: akamai:akamai-case-management-api
    name: Akamai Case Management API
    tags: []
    humanURL: https://techdocs.akamai.com/case-mgmt/reference/api
    properties:
      - url: https://techdocs.akamai.com/case-mgmt/reference/api
        type: Documentation
    description: >-
      Manage support requests to resolve any issues with your Akamai
      applications and services using the Case Management API.
  - aid: akamai:akamai-certificate-provisioning-system-api
    name: Akamai Certificate Provisioning System API
    tags: []
    humanURL: https://techdocs.akamai.com/cps/reference/api
    properties:
      - url: https://techdocs.akamai.com/cps/reference/api
        type: Documentation
    description: >-
      The Certificate Provisioning System (CPS) provides full life cycle
      management of SSL/TLS certificates for your Akamai Secure Delivery Network
      applications. This includes ability to request new certificates, modify
      existing certificates, automatically renew certificates, and delete
      certificates. CPS also manages key Transport Layer Security (TLS)
      configurations, including cipher selection.
  - aid: akamai:akamai-client-access-control-api
    name: Akamai Client Access Control API
    tags: []
    humanURL: https://techdocs.akamai.com/client-access-control/reference/api
    properties:
      - url: https://techdocs.akamai.com/client-access-control/reference/api
        type: Documentation
    description: >-
      The Client Access Control (CAC) API helps you manage access between your
      web assets and the edge servers on the Akamai network. With this API you
      can retrieve information about the CIDR blocks that currently connect your
      content to the Akamai network. In addition, when Akamai updates the CIDR
      blocks used for access, this API allows you to review the changes and send
      an acknowledgement to Akamai once you update your Access Control List
      (ACL).
  - aid: akamai:akamai-cloud-access-manager-api
    name: Akamai Cloud Access Manager API
    tags: []
    humanURL: https://techdocs.akamai.com/cloud-access-mgr/reference/api
    properties:
      - url: https://techdocs.akamai.com/cloud-access-mgr/reference/api
        type: Documentation
    description: >-
      The Cloud Access Manager (CAM) API connects the Akamai Intelligent
      Platform and your cloud provider. Use CAM to enable cloud origin
      authentication and securely store and manage your cloud provider origin
      credentials as access keys. You can easily select an access key in the
      Origin Characteristics behavior when creating a Property Manager property
      for your Akamai product, eliminating the need to manually provide the
      credentials. You can use the same access key between several properties,
      for Akamai products that offer support for the Origin Characteristics
      behavior.
  - aid: akamai:akamai-cloud-wrapper-configuration-api
    name: Akamai Cloud Wrapper Configuration API
    tags: []
    humanURL: https://techdocs.akamai.com/cloud-wrapper/reference/api
    properties:
      - url: https://techdocs.akamai.com/cloud-wrapper/reference/api
        type: Documentation
    description: >-
      Use Cloud Wrapper to reduce origin requests by optimizing connectivity
      between cloud infrastructures and the Akamai Intelligent Edge.
  - aid: akamai:akamai-cloudlets-api-v3
    name: Akamai Cloudlets API v3
    tags: []
    humanURL: https://techdocs.akamai.com/cloudlets/reference/api
    properties:
      - url: https://techdocs.akamai.com/cloudlets/reference/api
        type: Documentation
    description: >-
      Cloudlets are value-added applications that complement Akamais core
      delivery solutions to solve specific business challenges. Cloudlets bring
      a sites business logic closer to the end user by placing it on the edge of
      the content delivery platform.
  - aid: akamai:akamai-cloudtest-api
    name: Akamai CloudTest API
    tags: []
    humanURL: https://techdocs.akamai.com/cloudtest/reference/api
    properties:
      - url: https://techdocs.akamai.com/cloudtest/reference/api
        type: Documentation
    description: >-
      You can use the CloudTest API service to plan for peak traffic performance
      by performance testing your environment safely and at scale to identify
      areas in your site or app that need strengthening. To have success with
      this API you need to first create your tests and other content in the
      CloudTest UI and understand the concepts there.
  - aid: akamai:akamai-contract-api
    name: Akamai Contract API
    tags: []
    humanURL: https://techdocs.akamai.com/contract-api/reference/api
    properties:
      - url: https://techdocs.akamai.com/contract-api/reference/api
        type: Documentation
    description: >-
      The Contract API provides information about Akamai contracts and the
      products included in those contracts. With this API, you can retrieve
      product information for a specified time frame by contract ID or reporting
      group.
  - aid: akamai:akamai-cp-codes-and-reporting-groups-api
    name: Akamai CP Codes and Reporting Groups API
    tags: []
    humanURL: https://techdocs.akamai.com/cp-codes/reference/api
    properties:
      - url: https://techdocs.akamai.com/cp-codes/reference/api
        type: Documentation
    description: >-
      The CP Codes and Reporting Groups API offers a programmatic interface to
      manage CP codes and reporting groups. It also details contracts and
      products associated with each CP code, and contracts and CP codes
      associated with each reporting group.
  - aid: akamai:akamai-datastream-2-api-v2
    name: Akamai DataStream 2 API v2
    tags: []
    humanURL: https://techdocs.akamai.com/datastream2/reference/api
    properties:
      - url: https://techdocs.akamai.com/datastream2/reference/api
        type: Documentation
    description: >-
      Now you can use the new version of the DataStream 2 API to capture log
      data and deliver them to a destination of your choice at low latency. We
      have redesigned the DataStream API for improved experience, including new
      features such as Patching streams.
  - aid: akamai:akamai-edge-diagnostics-api
    name: Akamai Edge Diagnostics API
    tags: []
    humanURL: >-
      https://techdocs.akamai.com/edge-diagnostics/reference/edge-diagnostics-api-1
    properties:
      - url: >-
          https://techdocs.akamai.com/edge-diagnostics/reference/edge-diagnostics-api-1
        type: Documentation
    description: >-
      Edge Diagnostics allows you to diagnose your server, DNS, and network
      problems from Akamai servers around the world.Once you extend your web
      content onto the Akamai edge network and apply various Akamai features to
      accelerate and manipulate content, you need to be able to troubleshoot any
      problems your users may encounter. With Edge Diagnostics API you can
      diagnose common problems you may experience when delivering content to
      your users, except for China CDN.
  - aid: akamai:akamai-edge-dns-api-v2
    name: Akamai Edge DNS API v2
    tags: []
    humanURL: https://techdocs.akamai.com/edge-dns/reference/edge-dns-api
    properties:
      - url: https://techdocs.akamai.com/edge-dns/reference/edge-dns-api
        type: Documentation
    description: >-
      Welcome to Akamai Edge DNS service. Edge DNS integrates easily with your
      existing DNS infrastructure to provide a secure, high performance, highly
      available and scalable solution for DNS hosting. As part of this service,
      Akamai runs name servers in multiple networks and in many geographic
      locations that are capable of resolving queries for your zones. Akamai IP
      Anycast technology is also capable of providing an unprecedented level of
      reliability and performance for name resolution.
  - aid: akamai:akamai-edgekv-api
    name: Akamai EdgeKV API
    tags: []
    humanURL: https://techdocs.akamai.com/edgekv/reference/api
    properties:
      - url: https://techdocs.akamai.com/edgekv/reference/api
        type: Documentation
    description: >-
      You can use the administrative APIs to control EdgeKV database functions
      outside EdgeWorkers JavaScript code. The APIs enable you to perform
      day-to-day operations, including creating new namespaces, updating data,
      deleting data, and managing access tokens.
  - aid: akamai:akamai-edgeworkers-api
    name: Akamai EdgeWorkers API
    tags: []
    humanURL: https://techdocs.akamai.com/edgeworkers/reference/api
    properties:
      - url: https://techdocs.akamai.com/edgeworkers/reference/api
        type: Documentation
    description: >-
      You can use the EdgeWorkers service to run JavaScript at the edge of the
      Internet to dynamically manage web traffic. You can use the EdgeWorkers
      API to deploy custom code on thousands of edge servers and apply logic
      that creates powerful web experiences.
  - aid: akamai:akamai-enhanced-content-control-utility-eccu-api
    name: Akamai Enhanced Content Control Utility (ECCU) API
    tags: []
    humanURL: https://techdocs.akamai.com/eccu/reference/api
    properties:
      - url: https://techdocs.akamai.com/eccu/reference/api
        type: Documentation
    description: >-
      The Enhanced Content Control Utility (ECCU) is one of several supported
      Akamai purge interfaces. Use ECCU to specify the set of files to refresh
      on the edge network. Specify directories, file extensions, certain types
      of HTTP request, or response properties to refine the set of content to
      refresh. For example, you can refresh specific parts of a library or the
      complete cache repository for many domains. The ECCU only invalidates
      content. It doesnt remove content from cache.
  - aid: akamai:akamai-enterprise-application-access-api
    name: Akamai Enterprise Application Access API
    tags: []
    humanURL: https://techdocs.akamai.com/eaa-api/reference/api
    properties:
      - url: https://techdocs.akamai.com/eaa-api/reference/api
        type: Documentation
    description: >-
      Enterprise Application Access allows you to integrate data path
      protection, single sign-on, identity access, application security, and
      management visibility and control for enterprise applications. EAA
      delivers access to applications, not the entire network. With EAA, users
      dont access applications directlyinstead, apps are hidden from the
      Internet and public exposure by closing all inbound firewall ports while
      providing authenticated end-users with access to only their own special
      applications.
  - aid: akamai:akamai-event-center-api
    name: Akamai Event Center API
    tags: []
    humanURL: https://techdocs.akamai.com/event-ctr/reference/api
    properties:
      - url: https://techdocs.akamai.com/event-ctr/reference/api
        type: Documentation
    description: >-
      The Event Center API lets you access and manage event data available in
      Akamai Control Center for the contract type and account.This API offers a
      programmatic alternative to many of the features available in the Event
      Center application in Control Center.
  - aid: akamai:akamai-event-viewer-api
    name: Akamai Event Viewer API
    tags: []
    humanURL: https://techdocs.akamai.com/event-viewer/reference/api
    properties:
      - url: https://techdocs.akamai.com/event-viewer/reference/api
        type: Documentation
    description: >-
      Event Viewer records events completed through Control Center that are
      available to site administrators, such as configuration changes, login
      attempts, and log deliveries.With the Event Viewer API, you can view a
      list of portal-visible events stored in the Event Logger system and
      related to a particular user account, optionally filtered by event type
      ID, date and time of an event, and event ID. You can also view all defined
      event types with related event definitions.
  - aid: akamai:akamai-fast-purge-api
    name: Akamai Fast Purge API
    tags: []
    humanURL: https://techdocs.akamai.com/purge-cache/reference/api
    properties:
      - url: https://techdocs.akamai.com/purge-cache/reference/api
        type: Documentation
    description: >-
      The Fast Purge API provides a programmatic interface for you to purge edge
      content. In this version, purge your own set of URLs or ARLs (Akamai
      resource locators), or any content grouped under a content provider (CP)
      code or cache tag. Delivery products such as Ion, Adaptive Media Delivery,
      Dynamic Delivery, and Dynamic Site Accelerator all support Fast Purge. If
      youre using a legacy Content Control Utility (CCU) API to purge content,
      see the migration instructions to convert your API programs to use Fast
      Purge.
  - aid: akamai:akamai-firewall-rules-notification-api
    name: Akamai Firewall Rules Notification API
    tags: []
    humanURL: https://techdocs.akamai.com/firewall-rules/reference/api
    properties:
      - url: https://techdocs.akamai.com/firewall-rules/reference/api
        type: Documentation
    description: >-
      Akamai periodically refreshes edge server IP addresses for routine
      maintenance. With Firewall Rules Notification, you can manage who receives
      email notifications about the planned changes. Akamai provides six to
      eight weeks of advance notice before activating the IP addresses.
  - aid: akamai:akamai-global-traffic-management-api
    name: Akamai Global Traffic Management API
    tags: []
    humanURL: https://techdocs.akamai.com/gtm/reference/api
    properties:
      - url: https://techdocs.akamai.com/gtm/reference/api
        type: Documentation
    description: >-
      The Internet domain name system (DNS) is a distributed system. It allows
      computer programs to issue queries about domain names which the DNS
      returns one or more answers to. The most common use for DNS is to convert
      hostnames, such as www.example.com, into IP addresses, which identify a
      particular computer at a particular Internet location. In the most
      traditional usage, a querys answers are static. Someone types the answers
      into a configuration file, and the answers change only when the file
      changes.
  - aid: akamai:akamai-global-traffic-management-load-feedback-api
    name: Akamai Global Traffic Management Load Feedback API
    tags: []
    humanURL: >-
      https://techdocs.akamai.com/gtm-load-feedback/reference/global-traffic-management-load-feedback-api
    properties:
      - url: >-
          https://techdocs.akamai.com/gtm-load-feedback/reference/global-traffic-management-load-feedback-api
        type: Documentation
    description: >-
      The Global Traffic Management Load Feedback API allows users to submit
      load data for a GTM domain in either JSON or XML format via POST, and to
      fetch the current load state via GET.
  - aid: akamai:akamai-global-traffic-management-reporting-api
    name: Akamai Global Traffic Management Reporting API
    tags: []
    humanURL: https://techdocs.akamai.com/gtm-reporting/reference/api
    properties:
      - url: https://techdocs.akamai.com/gtm-reporting/reference/api
        type: Documentation
    description: >-
      The Traffic Management Reporting API provides read-only reports on GTMs
      real time statistics. Each call allows you to view traffic, liveness,
      direct demand, load feedback, and latency on datacenters and
      properties.This API is for site administrators, project managers,
      technical support providers, and others who implement traffic management
      reporting for your organization. It assumes that you have a working
      knowledge of traffic management reporting and GTM.
  - aid: akamai:akamai-identity-and-access-management-api-v3
    name: Akamai Identity and Access Management API v3
    tags: []
    humanURL: https://techdocs.akamai.com/iam-api/reference/api
    properties:
      - url: https://techdocs.akamai.com/iam-api/reference/api
        type: Documentation
    description: 'null'
  - aid: akamai:akamai-identity-cloud-authentication-api
    name: Akamai Identity Cloud Authentication API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-auth/reference/api
    properties:
      - url: https://techdocs.akamai.com/identity-cloud-auth/reference/api
        type: Documentation
    description: >-
      The Authentication API provides methods for creating accounts on, and
      logging in to, websites and apps. Users can create these accounts, and log
      in, by using one of two approaches:
  - aid: akamai:akamai-identity-cloud-configuration-api
    name: Akamai Identity Cloud Configuration API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-config/reference/api
    properties:
      - url: https://techdocs.akamai.com/identity-cloud-config/reference/api
        type: Documentation
    description: >-
      The Configuration API is a large collection of endpoints revolving around
      three areas of Identity Cloud administration:
  - aid: akamai:akamai-identity-cloud-custom-provider-api
    name: Akamai Identity Cloud Custom Provider API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-custom-provider/reference/api
    properties:
      - url: >-
          https://techdocs.akamai.com/identity-cloud-custom-provider/reference/api
        type: Documentation
    description: >-
      Social login and registration enables users to register and login to your
      website by using an account created on a social login identity provider
      (IdP) such as Facebook or Twitter. For example, instead of logging on by
      using an email address and password users can log on by using their
      Facebook account or their Twitter account.
  - aid: akamai:akamai-identity-cloud-entity-and-entitytype-api
    name: Akamai Identity Cloud Entity and EntityType API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-entity/reference/api
    properties:
      - url: https://techdocs.akamai.com/identity-cloud-entity/reference/api
        type: Documentation
    description: >-
      Identity Cloud uses its own terminology when referring to user accounts
      and to the databases where user account information is stored. In Identity
      Cloud, the term entity is used when referencing user accounts and user
      profiles. As you might expect then, the /entity.create operation is used
      to create user accounts and the /entity.find operation is used to search
      for user accounts.
  - aid: akamai:akamai-identity-cloud-hosted-login-api
    name: Akamai Identity Cloud Hosted Login API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-hosted-login/reference/api
    properties:
      - url: https://techdocs.akamai.com/identity-cloud-hosted-login/reference/api
        type: Documentation
    description: >-
      The Hosted Login, OAuth 2.0, and OpenID Connect APIs represent your
      primary toolset for managing Hosted Login. Most Hosted Login management
      tasks can only be carried out by using API calls. Keep in mind, too that
      some Hosted Login management tasks, such as managing two-factor
      authentication messages, or creating, modifying, and deleting Hosted Login
      links, require the use of other operations. For example, you need to use
      the Configuration API to manage two-factor authentication messages or
      Hosted Login Links.
  - aid: akamai:akamai-identity-cloud-siem-event-service-api
    name: Akamai Identity Cloud SIEM Event Service API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-siem-delivery/reference/api
    properties:
      - url: https://techdocs.akamai.com/identity-cloud-siem-delivery/reference/api
        type: Documentation
    description: >-
      Security Event and Information Management (SIEM) is a recognized standard
      for collecting, aggregating, and analyzing events that take place on a
      website or within an app. Identity Clouds SIEM event delivery service can
      inform you, in near real-time, each time a specified event occurs. See
      Identity Cloud SIEM events for more information on the events available to
      the SIEM event service.
  - aid: akamai:akamai-identity-cloud-social-api
    name: Akamai Identity Cloud Social API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-social-login/reference/api
    properties:
      - url: https://techdocs.akamai.com/identity-cloud-social-login/reference/api
        type: Documentation
    description: >-
      The Social API manages and configures social login, the technology
      enabling users to create, and then log in to, an Identity Cloud website by
      using their Facebook account, their Twitter account, or an account created
      with any of the other supported social login identity providers. The API
      itself consists of a number of different operations, including:
  - aid: akamai:akamai-identity-cloud-webhooks-v3-api
    name: Akamai Identity Cloud Webhooks v3 API
    tags: []
    humanURL: https://techdocs.akamai.com/identity-cloud-webhooks/reference/api
    properties:
      - url: https://techdocs.akamai.com/identity-cloud-webhooks/reference/api
        type: Documentation
    description: >-
      Webhooks v3 sends you near real-time notifications any time a user account
      is created, deleted, or modified. Sometimes these notifications are
      invaluable in safeguarding your website. For example, a sudden and
      unexpected flurry of password changes could indicate that your security
      has been breached and a malefactor is busy changing all your user
      passwords.
  - aid: akamai:akamai-image-and-video-manager-api
    name: Akamai Image and Video Manager API
    tags: []
    humanURL: https://techdocs.akamai.com/ivm/reference/api
    properties:
      - url: https://techdocs.akamai.com/ivm/reference/api
        type: Documentation
    description: >-
      Image and Video Manager transforms a websites images by creating
      derivative images of various sizes and formats, and dynamically selecting
      the best image when requested by an end user.The API offers an end-to-end
      solution to archive, manage, and deliver transformed images based on
      customer defined policies.
  - aid: akamai:akamai-invoicing-api-v4
    name: Akamai Invoicing API v4
    tags: []
    humanURL: https://techdocs.akamai.com/invoicing/reference/api
    properties:
      - url: https://techdocs.akamai.com/invoicing/reference/api
        type: Documentation
    description: >-
      The Invoicing API provides data about your Akamai invoices and credit
      memos.This API offers a programmatic alternative to the Your bills, Bills
      history, and Notifications features available in the Billing Akamai
      Control Center interface.
  - aid: akamai:akamai-ion
    name: Akamai Ion
    tags: []
    humanURL: https://techdocs.akamai.com/ion/docs/welcome-ion
    properties:
      - url: https://techdocs.akamai.com/ion/docs/welcome-ion
        type: Documentation
    description: >-
      Ion is a suite of intelligent performance optimizations and controls that
      help to deliver superior website and iOS or Android app experiences. It
      combines the scalability of Akamais global content delivery platform with
      fast, dynamic content acceleration. Ion also leverages Akamais cellular
      optimizations, which lower both latency and user engagement disruptions.
  - aid: akamai:akamai-iot-ota-updates-api
    name: Akamai IoT OTA Updates API
    tags: []
    humanURL: https://techdocs.akamai.com/iot-ota-updates/reference/api
    properties:
      - url: https://techdocs.akamai.com/iot-ota-updates/reference/api
        type: Documentation
    description: >-
      Part of the Internet of Things (IoT) product, the OTA Updates module
      enables automotive companies to leverage the Akamai Intelligent Platform
      to provide a highly scalable, secure, and reliable mechanism to update
      software on vehicle head units over a cellular network.
  - aid: akamai:akamai-iot-token-access-control-api
    name: Akamai IoT Token Access Control API
    tags: []
    humanURL: https://techdocs.akamai.com/iot-token-access-control/reference/api
    properties:
      - url: https://techdocs.akamai.com/iot-token-access-control/reference/api
        type: Documentation
    description: >-
      The Token Access Control API allows you to programmatically create,
      manage, and store collections of public keys. It lets you upload public
      keys into key collections, activate key collections in the staging
      environment before going live, and create key collection versions to
      enable frictionless public key rotation for property configurations.
  - aid: akamai:akamai-linode-api
    name: Akamai Linode API
    tags: []
    humanURL: https://techdocs.akamai.com/linode-api/reference/api
    properties:
      - url: https://techdocs.akamai.com/linode-api/reference/api
        type: Documentation
    description: >-
      The Linode API lets you programmatically manage the full range of Akamai
      cloud computing products and services. Here are a few of the things you
      can do with this API:
  - aid: akamai:akamai-live-archive-management-api
    name: Akamai Live Archive Management API
    tags: []
    humanURL: https://techdocs.akamai.com/live-archive-management/reference/api
    properties:
      - url: https://techdocs.akamai.com/live-archive-management/reference/api
        type: Documentation
    description: >-
      Media Services Live 4 lets you archive live streams in HLS and DASH
      formats for use as video on demand (VOD) content. You can use the Live
      Archive Management (LAM) API to do multiple things:
  - aid: akamai:akamai-media-delivery-reports-api
    name: Akamai Media Delivery Reports API
    tags: []
    humanURL: >-
      https://techdocs.akamai.com/media-delivery-rpts/reference/media-delivery-reports
    properties:
      - url: >-
          https://techdocs.akamai.com/media-delivery-rpts/reference/media-delivery-reports
        type: Documentation
    description: >-
      Media Delivery Reports let you monitor and identify key trends of your
      Akamai delivery solutions, including Adaptive Media Delivery, Download
      Delivery, Object Delivery, and Akamai Cloud Embed (formerly Wholesale
      Delivery). These reports offer valuable insights to enhance your business
      by optimizing your streaming content, software downloads, and object
      delivery.
  - aid: akamai:akamai-media-services-live-reports-api
    name: Akamai Media Services Live Reports API
    tags: []
    humanURL: >-
      https://techdocs.akamai.com/media-services-rpts/reference/media-services-reports-api
    properties:
      - url: >-
          https://techdocs.akamai.com/media-services-rpts/reference/media-services-reports-api
        type: Documentation
    description: >-
      This API lets you monitor traffic for your Media Services Live 4 streams.
      These first-mile reports provide information on ingest quality,
      availability, and accelerated streams.
  - aid: akamai:akamai-media-services-live-stream-provisioning-api
    name: Akamai Media Services Live Stream Provisioning API
    tags: []
    humanURL: https://techdocs.akamai.com/msl/reference/api
    properties:
      - url: https://techdocs.akamai.com/msl/reference/api
        type: Documentation
    description: >-
      The Media Services Live (MSL) Stream Provisioning API lets you publish
      live streaming media content and retrieve it through the Akamai
      Intelligent Edge Platform or any content delivery network (CDN). These
      operations are targeted primarily for Over-the-top (OTT) applications, but
      can also be used for other live streaming events.
  - aid: akamai:akamai-mpulse-api
    name: Akamai mPulse API
    tags: []
    humanURL: https://techdocs.akamai.com/mpulse/reference/api
    properties:
      - url: https://techdocs.akamai.com/mpulse/reference/api
        type: Documentation
    description: >-
      You can use the mPulse API service to view real-time analytics and user
      measurement beacons for web sites to observe how real users interact
      within your sites.
  - aid: akamai:akamai-mutual-tls-edge-truststore-api
    name: Akamai Mutual TLS Edge Truststore API
    tags: []
    humanURL: https://techdocs.akamai.com/mtls-edge-truststore/reference/api
    properties:
      - url: https://techdocs.akamai.com/mtls-edge-truststore/reference/api
        type: Documentation
    description: >-
      You can use Mutual TLS Edge Truststore API to create, manage, and activate
      certificate (CA) sets needed to set up mutual authentication (mTLS)
      sessions between a client and Akamai edge servers.Each CA set contains a
      collection of certificates that validate the client certificates presented
      by a user during mTLS  thats the TLS handshake at the edge server.
  - aid: akamai:akamai-mutual-tls-origin-keystore-api
    name: Akamai Mutual TLS Origin Keystore API
    tags: []
    humanURL: https://techdocs.akamai.com/mtls-origin-keystore/reference/api
    properties:
      - url: https://techdocs.akamai.com/mtls-origin-keystore/reference/api
        type: Documentation
    description: >-
      You can use the Mutual TLS Origin Keystore API to create, manage, and
      activate client certificates needed to set up mutual authentication (mTLS)
      sessions between the origin and Akamai edge servers.
  - aid: akamai:akamai-netstorage-configuration-api
    name: Akamai NetStorage Configuration API
    tags: []
    humanURL: https://techdocs.akamai.com/netstorage/reference/api
    properties:
      - url: https://techdocs.akamai.com/netstorage/reference/api
        type: Documentation
    description: >-
      NetStorage is a managed service that provides persistent, replicated
      storage of website content, including images, streaming media files,
      software, documents, and other digital objects. Content replicates
      periodically to core network locations to make it highly available to, and
      easily accessible by, EdgePlatform servers. NetStorage complements
      multiple content delivery services.
  - aid: akamai:akamai-netstorage-usage-api
    name: Akamai NetStorage Usage API
    tags: []
    humanURL: https://techdocs.akamai.com/netstorage-usage/reference/api
    properties:
      - url: https://techdocs.akamai.com/netstorage-usage/reference/api
        type: Documentation
    description: >-
      This API provides various HTTP methods you can use to manage your
      NetStorage content. Communication uses the Edge network using a HTTP(S)
      client of your own design. The client could be a web-based browser or
      scripted tools integrated with your content management system so long as
      each request provides the required HTTP headers.
  - aid: akamai:akamai-network-lists-api
    name: Akamai Network Lists API
    tags: []
    humanURL: https://techdocs.akamai.com/network-lists/reference/api
    properties:
      - url: https://techdocs.akamai.com/network-lists/reference/api
        type: Documentation
    description: >-
      The Network Lists API allows you to manage a common set of lists for use
      in various Akamai security products such as Kona Site Defender, Web App
      Protector, and Bot Manager. Network lists are shared sets of IP addresses,
      CIDR blocks, or broad geographic areas. Along with managing your own
      lists, you can also access read-only lists that Akamai dynamically updates
      for you.
  - aid: akamai:akamai-prolexic-analytics-api
    name: Akamai Prolexic Analytics API
    tags: []
    humanURL: https://techdocs.akamai.com/prolexic/reference/api
    properties:
      - url: https://techdocs.akamai.com/prolexic/reference/api
        type: Documentation
    description: >-
      The Prolexic Analytics API exposes analytics data from Prolexic DDoS
      protection and monitoring services, such as IP Protect, which provides
      alerts and network bandwidth time-series data.
  - aid: akamai:akamai-prolexic-ip-protect-configuration-api
    name: Akamai Prolexic IP Protect Configuration API
    tags: []
    humanURL: https://techdocs.akamai.com/ip-protect/reference/api
    properties:
      - url: https://techdocs.akamai.com/ip-protect/reference/api
        type: Documentation
    description: >-
      Prolexic IP Protect helps shield your site from DDoS attacks: attempts to
      disrupt your website by overwhelming it with Internet traffic. With IP
      Protect that isnt a problem, because most Internet traffic doesnt go
      directly to your website. Instead:
  - aid: akamai:akamai-property-manager-api
    name: Akamai Property Manager API
    tags: []
    humanURL: https://techdocs.akamai.com/property-mgr/reference/api
    properties:
      - url: https://techdocs.akamai.com/property-mgr/reference/api
        type: Documentation
    description: >-
      The Property Manager API (PAPI) offers a programmatic interface to manage
      how Akamai edge servers process requests, responses, and objects served
      over the Akamai platform. A distributed property configuration collects
      all the rules for how to process end-user requests for your web assets.
      Like Property Manager in Akamai Control Center, this API lets you modify
      your property configurations and activate them on Akamai staging or
      production networks. The API allows you to access the same features
      rapidly and flexibly using your own tools. With PAPI, you can generate
      properties, associate them with dynamically generated hostnames, and
      create new CP codes to report on your contents traffic. PAPI also provides
      bulk update capabilities for modifying and activating many properties at
      once, and includes that let you split huge property configurations into
      smaller, reusable chunks.
  - aid: akamai:akamai-reporting-api
    name: Akamai Reporting API
    tags: []
    humanURL: https://techdocs.akamai.com/reporting/reference/api
    properties:
      - url: https://techdocs.akamai.com/reporting/reference/api
        type: Documentation
    description: >-
      If youre using Akamai Intelligent Platform to deliver your content, you
      want to see how its performing. The Reporting API provides a wide range of
      reports, with new reports added periodically, and allows you to retrieve
      data in a range of intervals, from five minutes to monthly, depending on
      the time period and type of data you want to view. Some reports are
      available only to those who have purchased the related product. Support
      for specific intervals, filters, and metrics may vary by report type.
  - aid: akamai:akamai-sandbox-api
    name: Akamai Sandbox API
    tags: []
    humanURL: https://techdocs.akamai.com/sandbox/reference/api
    properties:
      - url: https://techdocs.akamai.com/sandbox/reference/api
        type: Documentation
    description: >-
      Resolving issues with your website and applications after a property is
      pushed to the content delivery network is inefficient and a drain on
      resources. With Sandbox, you can tweak your site delivery options and test
      in an isolated development environment to identify issues locally before
      merging.Incorporate the Sandbox API into your agile development workflow
      to improve efficiency and identify potential issues well in advance of
      deployment. You can quickly test and validate code changes on your local
      development server through a secure connection to your sandbox.
  - aid: akamai:akamai-script-management-api
    name: Akamai Script Management API
    tags: []
    humanURL: https://techdocs.akamai.com/script-management/reference/api
    properties:
      - url: https://techdocs.akamai.com/script-management/reference/api
        type: Documentation
    description: >-
      Use the Script Management API to create and view policies. These policies
      can help minimize performance impacts from third-party JavaScripts used by
      your site or app.
  - aid: akamai:akamai-secure-internet-access-enterprise-configuration-api-v3
    name: Akamai Secure Internet Access Enterprise Configuration API v3
    tags: []
    humanURL: https://techdocs.akamai.com/etp-config/reference/api
    properties:
      - url: https://techdocs.akamai.com/etp-config/reference/api
        type: Documentation
    description: >-
      The Secure Internet Access Enterprise (SIA) Configuration API offers a
      programmatic interface to manage policy settings to protect against
      enterprise security and acceptable user policy related events. A
      distributed configuration encapsulates all the rules for how to process
      DNS requests for your enterprise.
  - aid: akamai:akamai-secure-internet-access-enterprise-reporting-api-v3
    name: Akamai Secure Internet Access Enterprise Reporting API v3
    tags: []
    humanURL: https://techdocs.akamai.com/etp-reporting/reference/api
    properties:
      - url: https://techdocs.akamai.com/etp-reporting/reference/api
        type: Documentation
    description: >-
      The Secure Internet Access Enterprise (SIA) Reporting API lets you access
      and analyze reports for acceptable user policy (AUP) events, DNS activity,
      network traffic connections, security connector events, and threat events.
      This API allows flexible access to reporting features in Akamai Control
      Center, using your own tools.
  - aid: akamai:akamai-service-level-agreement-api
    name: Akamai Service-Level Agreement API
    tags: []
    humanURL: https://techdocs.akamai.com/sla/reference/api
    properties:
      - url: https://techdocs.akamai.com/sla/reference/api
        type: Documentation
    description: >-
      The service-level agreement (SLA) API provides programmatic access to SLA
      test configurations and the resulting reports.SLA tests measure certain
      availability and performance metrics. The results of these tests can help
      you check whether Akamai is achieving the performance gains and platform
      availability set forth in the SLA included with your purchase contract.
  - aid: akamai:akamai-siem-integration-api
    name: Akamai SIEM Integration API
    tags: []
    humanURL: https://techdocs.akamai.com/siem-integration/reference/api
    properties:
      - url: https://techdocs.akamai.com/siem-integration/reference/api
        type: Documentation
    description: >-
      The Security Information and Event Management API allows you to capture
      security events generated on the Akamai platform in your SIEM application.
  - aid: akamai:akamai-single-sign-on-configuration-api
    name: Akamai Single Sign-On Configuration API
    tags: []
    humanURL: https://techdocs.akamai.com/sso-config/reference/api
    properties:
      - url: https://techdocs.akamai.com/sso-config/reference/api
        type: Documentation
    description: >-
      If youre an administrator who handles Akamai portal accounts and users,
      use this API to manage your IdP (identity provider) certificates. For
      details on how to manage all functions and information related to SSO, see
      Get started with SSO with SAML.
  - aid: akamai:akamai-site-shield-api
    name: Akamai Site Shield API
    tags: []
    humanURL: https://techdocs.akamai.com/site-shield/reference/api
    properties:
      - url: https://techdocs.akamai.com/site-shield/reference/api
        type: Documentation
    description: >-
      The Site Shield API offers a programmatic interface that provides an
      additional layer of defense for your critical websites and web
      applications. This API removes websites and applications from
      internet-accessible IP address space and prevents attackers from directly
      accessing the origin. Instead, clients must go through the Akamai
      Intelligent Platform, where attacks are detected and mitigated.
  - aid: akamai:akamai-test-center-api
    name: Akamai Test Center API
    tags: []
    humanURL: https://techdocs.akamai.com/test-ctr/reference/api
    properties:
      - url: https://techdocs.akamai.com/test-ctr/reference/api
        type: Documentation
    description: >-
      Test Center allows you to test how configuration changes affect your web
      content on Akamai edge network. Prior to activation, you can check to make
      sure theyre not behaving in an unexpected manner. This testing tool helps
      to prevent issues caused by misconfiguration and insufficient testing,
      increasing your confidence in the safety and correctness of your
      configuration changes.
name: Akamai
tags:
  - Cloud
  - Networks
  - CDN
  - Platform
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
common:
  - data:
      numberOfAPITags: 4
      numberOfAPIPaths: 0
      numberOfAPISchema: 0
      numberOfAPIGetMethods: 0
      numberOfAPIParameters: 0
      numberOfAPIProperties: 0
      numberOfAPIPutMethods: 0
      numberOfAPIPostMethods: 0
      numberOfAPIPatchMethods: 0
      numberOfAPIDeleteMethods: 0
      numberOfAPIOptionMethods: 0
    type: Summary
created: '2025-01-08'
modified: '2025-02-26'
position: Consumer
description: >-
  Akamai is a global content delivery network (CDN) and cloud service provider
  that helps organizations deliver secure, high-performing digital experiences
  to their users. By utilizing their extensive network of servers located around
  the world, Akamai helps to speed up the delivery of content, applications, and
  videos, while also ensuring a reliable and secure online experience for users.
  Their services range from web performance optimization and security solutions
  to video delivery and cloud security, making them a trusted partner for
  organizations looking to improve their online presence and user engagement.
  With Akamai's technology and expertise, businesses can better reach and
  connect with their customers, no matter where they are located.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
specificationVersion: '0.19'

---