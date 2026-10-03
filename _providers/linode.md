---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 326
  human_in_the_loop: 21
  name: Linode Agentic Access
  operation_count: 655
  slug: linode-agentic-access
  summary_line: 655 operations · 326 acting · 21 human-in-the-loop
api_count: 2
apis:
- description: The Linode CLI is a command-line interface that wraps the Linode API v4, allowing developers and system administrators to manage Akamai Connected Cloud resources directly from the terminal. It support
  name: Linode CLI
  slug: cli
- description: The Linode Python SDK (linode_api4) is the official Python client library for interacting with the Linode API v4. It provides a Pythonic interface for managing all Akamai Connected Cloud resources inc
  name: Linode Python SDK
  slug: python-sdk
- description: The Linode Go SDK (linodego) is the official Go client library for the Linode API v4. It provides idiomatic Go interfaces for managing Akamai Connected Cloud infrastructure programmatically, including
  name: Linode Go SDK
  slug: go-sdk
- description: The Linode Terraform Provider enables infrastructure-as-code management of Akamai Connected Cloud resources using HashiCorp Terraform. It supports provisioning and managing compute instances, Kubernet
  name: Linode Terraform Provider
  slug: terraform-provider
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage your account settings, users, billing information, OAuth clients, service transfers, and payment methods.
  name: linode Account API
  slug: linode-account-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Managed Database instances including MySQL and PostgreSQL clusters, backups, credentials, and maintenance windows.
  name: linode Databases API
  slug: linode-databases-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage DNS domains and their associated resource records including A, AAAA, CNAME, MX, TXT, SRV, CAA, and NS records.
  name: linode Domains API
  slug: linode-domains-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage custom images for deploying Linode instances, including creating images from disks, uploading images, and managing image metadata.
  name: linode Images API
  slug: linode-images-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage Linode compute instances, including configuration profiles, disks, backups, networking, migration, resize, and rebuild operations.
  name: linode Instances API
  slug: linode-linode-instances-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Deploy and manage Kubernetes clusters, node pools, and cluster configurations through the Linode Kubernetes Engine.
  name: linode Kubernetes Engine (LKE) API
  slug: linode-linode-kubernetes-engine-lke-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Longview clients and subscriptions for system-level monitoring and metrics collection on Linode instances.
  name: linode Longview API
  slug: linode-longview-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Linode Managed services including monitored contacts, credentials, issues, service monitors, and SSH access settings.
  name: linode Managed API
  slug: linode-managed-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage networking resources including IP addresses, IPv6 ranges and pools, firewalls, VLANs, and IP address sharing and assignment.
  name: linode Networking API
  slug: linode-networking-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage NodeBalancer load balancers, their configurations, and backend nodes for distributing traffic across Linode instances.
  name: linode NodeBalancers API
  slug: linode-nodebalancers-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage Object Storage buckets, access keys, clusters, and endpoints for S3-compatible object storage.
  name: linode Object Storage API
  slug: linode-object-storage-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage placement groups for controlling the physical placement of Linode instances within a data center.
  name: linode Placement Groups API
  slug: linode-placement-groups-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage your user profile settings, SSH keys, authorized applications, personal access tokens, and two-factor authentication.
  name: linode Profile API
  slug: linode-profile-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: List available data center regions and their capabilities for deploying Linode services.
  name: linode Regions API
  slug: linode-regions-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage StackScripts for automating the deployment and configuration of Linode instances.
  name: linode StackScripts API
  slug: linode-stackscripts-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage support tickets and view replies for getting help from the Linode support team.
  name: linode Support API
  slug: linode-support-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Tags API from linode — 2 operation(s) for tags.
  name: linode Tags API
  slug: linode-tags-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage Block Storage volumes that can be attached to Linode instances for persistent data storage.
  name: linode Volumes API
  slug: linode-volumes-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage Virtual Private Clouds for isolated network environments and subnets for Linode instances.
  name: linode VPCs API
  slug: linode-vpcs-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Object Storage keys are used to authenticate access to your Object Storage buckets. Use these operations to create, view, update, and revoke these keys.
  name: Linode Access keys API
  slug: linode-access-keys-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to review and manage any agreements you need to acknowledge to use the API's services.
  name: Linode Account agreements API
  slug: linode-account-agreements-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to review the services available for use with your account.
  name: Linode Account availability API
  slug: linode-account-availability-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to review successful login data.
  name: Linode Account logins API
  slug: linode-account-logins-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Account settings applies to various services available on your account, including Backups, Linode Interfaces, a Longview subscription, Maintenance Policy, our Managed service, Network Helper, and Obje
  name: Linode Account settings API
  slug: linode-account-settings-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Used to manage transfer objects that show your network utilization.
  name: Linode Account transfer API
  slug: linode-account-transfer-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Akamai Cloud Pulse lets you configure alerts to monitor key metrics and events in real time and automatically trigger notifications or actions when predefined thresholds or conditions are met.
  name: Linode Alerts API
  slug: linode-alerts-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Mange any attachments you may need to include with your support tickets, such as log entry files and screenshot images.
  name: Linode Attachments API
  slug: linode-attachments-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Buckets are the primary containers within Object Storage. Each bucket stores your files (objects) and lets you access or share those files. Use these operations to create and manage buckets, as well a
  name: Linode Buckets API
  slug: linode-buckets-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Child accounts let you, as an Akamai partner (a parent account holder), switch between and manage your end customers' accounts (child accounts). Talk to your account team about [setting up a parent-ch
  name: Linode Child accounts API
  slug: linode-child-accounts-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to upgrade and manage a legacy configuration profile on your Linode to include networking interfaces.
  name: Linode Configuration profile interfaces API
  slug: linode-configuration-profile-interfaces-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: A configuration profile establishes the disk layout, kernel installation, and other specifics for a Linode. This is the legacy method used to define a Linode's makeup, and it does not include networki
  name: Linode Configuration profiles API
  slug: linode-configuration-profiles-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Configurations API from Linode — 3 operation(s) for configurations.
  name: Linode Configurations API
  slug: linode-configurations-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View and manage access control lists (ACLs) for the control planes on your LKE clusters. Control Plane ACLs allow you to restrict access to your cluster's control plane to specific IP addresses or ran
  name: Linode Control Plane ACL API
  slug: linode-control-plane-acl-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to manage delegations for [parent and child accounts](https://techdocs.akamai.com/cloud-computing/docs/parent-and-child-accounts-for-akamai-partners).
  name: Linode Delegation for parent and child accounts API
  slug: linode-delegation-for-parent-and-child-accounts-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Devices API from Linode — 2 operation(s) for devices.
  name: Linode Devices API
  slug: linode-devices-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to create and manage domain records on your account.
  name: Linode Domain records API
  slug: linode-domain-records-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: These operations involve viewing specifics for a domain zone file.
  name: Linode Domain zone files API
  slug: linode-domain-zone-files-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: An endpoint is the S3-compatible URL to an Object Storage bucket. Use these operations to review details about your endpoints.
  name: Linode Endpoints API
  slug: linode-endpoints-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: These legacy operations are available to review and manage the transfer of one entity to another. These operations have been deprecated. Use the Service transfers category operations instead.
  name: Linode Entity transfers API
  slug: linode-entity-transfers-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: An event represents an action you've taken on your account, over the last 90 days. Use these operations to review your current events.
  name: Linode Events API
  slug: linode-events-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Firewall settings API from Linode — 1 operation(s) for firewall settings.
  name: Linode Firewall settings API
  slug: linode-firewall-settings-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Firewalls API from Linode — 6 operation(s) for firewalls.
  name: Linode Firewalls API
  slug: linode-firewalls-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Object Storage is Akamai cloud computing's S3-compatible data storage service. Use these operations to review and manage your Object Storage service.
  name: Linode General API
  slug: linode-general-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View the grants (permissions) available to your user account.
  name: Linode Grants API
  slug: linode-grants-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to manage access to entities and roles on your account.
  name: Linode Identity Management API
  slug: linode-identity-management-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use the Identity Management IDP Configuration endpoints to configure SAML-based Single Sign-On (SSO) for your account. You can create and manage an external identity provider (IDP) configuration, cont
  name: Linode IDP configuration API
  slug: linode-idp-configuration-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to create and mange groups of users that can access your stored images.
  name: Linode Image sharing API
  slug: linode-image-sharing-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Review invoice and billing data for services on your account.
  name: Linode Invoices API
  slug: linode-invoices-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: 'Use the IP addresses endpoints to view Virtual Private Cloud (VPC): - IP addresses - default address ranges - forbidden CIDR blocks for your environment'
  name: Linode IP addresses API
  slug: linode-ip-addresses-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The IPv4 addresses API from Linode — 2 operation(s) for ipv4 addresses.
  name: Linode IPv4 addresses API
  slug: linode-ipv4-addresses-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The IPv6 pools API from Linode — 1 operation(s) for ipv6 pools.
  name: Linode IPv6 pools API
  slug: linode-ipv6-pools-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The IPv6 ranges API from Linode — 2 operation(s) for ipv6 ranges.
  name: Linode IPv6 ranges API
  slug: linode-ipv6-ranges-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View or regenerate the kubeconfig files for your LKE clusters, which authenticate and configure access to your Kubernetes clusters.
  name: Linode Kubeconfigs API
  slug: linode-kubeconfigs-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Clusters refer to the legacy methodology Object Storage used, before moving Object Storage to our actual data centers (regions). These operations have been deprecated and only apply if you're still us
  name: Linode Legacy clusters API
  slug: linode-legacy-clusters-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Backups service lets you enable automatic backups of the disks on your Linodes. Use these operations to manage your backups.
  name: Linode Linode disk backups API
  slug: linode-linode-disk-backups-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to manage the individual disks on your Linode.
  name: Linode Linode disks API
  slug: linode-linode-disks-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to manage the firewalls applied to your Linodes.
  name: Linode Linode firewalls API
  slug: linode-linode-firewalls-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: A Linode interface lets you set up networking on your Linode. A Linode interface links to the Linode, rather than to a legacy configuration profile. Use these operations to manage the Linode interface
  name: Linode Linode interfaces API
  slug: linode-linode-interfaces-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to view and manage the IP addresses assigned to your Linodes.
  name: Linode Linode IP addresses API
  slug: linode-linode-ip-addresses-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to review information for the Linux kernels on your Linodes.
  name: Linode Linode kernels API
  slug: linode-linode-kernels-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: A NodeBalancer is a managed load balancer that intelligently distributes incoming requests to multiple backend Linodes, so that there's no single point of failure. Use these operations to review the N
  name: Linode Linode NodeBalancers API
  slug: linode-linode-nodebalancers-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to review various statistics for your Linodes.
  name: Linode Linode statistics API
  slug: linode-linode-statistics-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to get information about Linode plan types, including pricing information, hardware resources, and network transfer allotment.
  name: Linode Linode types API
  slug: linode-linode-types-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Block Storage service lets you add storage drives, called volumes to your Linodes. This lets you store more data without resizing your Linode to a larger plan. Use these operations to review the B
  name: Linode Linode volumes API
  slug: linode-linode-volumes-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View the API endpoints for your LKE clusters.
  name: Linode LKE API endpoints API
  slug: linode-lke-api-endpoints-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View the Kubernetes Dashboard URLs for your LKE clusters, which provides a web-based user interface for managing and monitoring each Kubernetes cluster.
  name: Linode LKE cluster dashboard API
  slug: linode-lke-cluster-dashboard-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage Kubernetes clusters on LKE (Linode Kubernetes Engine).
  name: Linode LKE clusters API
  slug: linode-lke-clusters-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create, manage, and configure node pools within your LKE clusters. Node pools allow you to group nodes with similar configurations and manage them collectively.
  name: Linode LKE node pools API
  slug: linode-lke-node-pools-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View, recycle, and delete nodes within your LKE clusters. Nodes are the worker machines in your Kubernetes cluster that run your containerized applications.
  name: Linode LKE nodes API
  slug: linode-lke-nodes-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Regenerate service account tokens for your LKE clusters, which are used by the cluster's control plane components and Linode CSI drivers to authenticate with the Kubernetes API server.
  name: Linode LKE service tokens API
  slug: linode-lke-service-tokens-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View the LKE tiers (types) available for your Kubernetes clusters. The cluster tier determines the control plane configuration and features available for your cluster.
  name: Linode LKE types API
  slug: linode-lke-types-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View the Kubernetes versions available for deployment on your LKE clusters.
  name: Linode LKE versions API
  slug: linode-lke-versions-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Akamai Cloud Pulse lets you capture log data across multiple Akamai Cloud services and deliver it to the destination of your choice. These logs can help you improve operational efficiency, enhance sec
  name: Linode Logs API
  slug: linode-logs-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create an manage Longview Clients to monitor the performance and health of your Linode instances and other servers.
  name: Linode Longview clients API
  slug: linode-longview-clients-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Get details on your current Longview plan subscription and, if needed, update your plan.
  name: Linode Longview plans API
  slug: linode-longview-plans-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Get publicly-accessible information about the Longview plans available on Akamai Cloud, including the number of supported clients.
  name: Linode Longview subscriptions API
  slug: linode-longview-subscriptions-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Get publicly-accessible information about the Longview plans available on Akamai Cloud, including network transfer and region-specific pricing.
  name: Linode Longview types API
  slug: linode-longview-types-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to view maintenance policies that are available for your Linodes.
  name: Linode Maintenance policies API
  slug: linode-maintenance-policies-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Review details on scheduled maintenance for your Akamai Cloud Computing services.
  name: Linode Maintenances API
  slug: linode-maintenances-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to view information about available beta programs and sign up to participate in them.
  name: Linode Manage Beta programs API
  slug: linode-manage-beta-programs-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage contacts associated with Linode Managed, who can be notified about issues with your managed Linodes.
  name: Linode Managed contacts API
  slug: linode-managed-contacts-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and manage credentials used by Linode Managed to access your Linodes for support and maintenance.
  name: Linode Managed credentials API
  slug: linode-managed-credentials-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View details about issues detected on your managed Linodes and their resolution status.
  name: Linode Managed issues API
  slug: linode-managed-issues-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View and update settings related to Linode Managed for each of your Linodes.
  name: Linode Managed Linode settings API
  slug: linode-managed-linode-settings-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Create and configure the service monitors that are used to check the health of your managed Linodes.
  name: Linode Managed service monitors API
  slug: linode-managed-service-monitors-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View the unique SSH public key assigned to your Linode Managed account.
  name: Linode Managed SSH keys API
  slug: linode-managed-ssh-keys-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View key metrics for your managed Linodes, including CPU usage, disk I/O, and network transfer.
  name: Linode Managed statistics API
  slug: linode-managed-statistics-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Akamai Cloud Pulse automatically collects and stores performance metrics for your cloud services. You can view them through dashboards and inspect them at the entity level. Metrics data provides insig
  name: Linode Metrics API
  slug: linode-metrics-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Managed Databases is Akamai's fully-managed, high-performance database service. Use these operations to create and manage clusters for MySQL engine databases.
  name: Linode My SQL API
  slug: linode-mysql-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Review network transfer pricing information.
  name: Linode Network transfer prices API
  slug: linode-network-transfer-prices-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The NodeBalancer types API from Linode — 1 operation(s) for nodebalancer types.
  name: Linode NodeBalancer types API
  slug: linode-nodebalancer-types-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Nodes API from Linode — 2 operation(s) for nodes.
  name: Linode Nodes API
  slug: linode-nodes-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Review notifications that represent important, often time-sensitive details about your account.
  name: Linode Notifications API
  slug: linode-notifications-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View authorized apps that have been granted access to your account. You can also revoke access for any authorized app.
  name: Linode OAuth apps API
  slug: linode-oauth-apps-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use an OAuth client to allow users (using their Akamai Cloud Computing account) to log in to your own application, and optionally grant your application some amount of access to their Akamai Cloud Com
  name: Linode OAuth clients API
  slug: linode-oauth-clients-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View and update user preferences tied to OAuth clients.
  name: Linode OAuth preferences API
  slug: linode-oauth-preferences-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Marketplace offers the Partner referrals program. This is a new space for Akamai qualified partners to offer their products to Cloud Manager customers.
  name: Linode Partner referrals API
  slug: linode-partner-referrals-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to review and manage the payment method you've set up to pay your invoices.
  name: Linode Payment methods API
  slug: linode-payment-methods-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to view current payment due information and make a payment.
  name: Linode Payments API
  slug: linode-payments-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage personal access tokens for your user account. Personal access tokens can be used for authentication with the Linode API.
  name: Linode Personal access tokens API
  slug: linode-personal-access-tokens-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Operations to verify and delete the phone number associated with your user account, which is used to send SMS messages as a form of two-factor authentication (2FA).
  name: Linode Phone number API
  slug: linode-phone-number-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Managed Databases is Akamai's fully-managed, high-performance database service. Use these operations to create and manage clusters for PostgreSQL engine databases.
  name: Linode Postgre SQL API
  slug: linode-postgresql-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Prefix Lists API from Linode — 3 operation(s) for prefix lists.
  name: Linode Prefix Lists API
  slug: linode-prefix-lists-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View a history of successful logins to your Linode account.
  name: Linode Profile logins API
  slug: linode-profile-logins-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to manage any promotional codes you've been granted for special offers.
  name: Linode Promo credits API
  slug: linode-promo-credits-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Quotas are limits related to your resource usage in Object Storage. Use these operations to review and manage your Object Storage quotas.
  name: Linode Quotas API
  slug: linode-quotas-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to create and view replies to correspondence for your support tickets.
  name: Linode Replies API
  slug: linode-replies-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Reserved IPs API from Linode — 3 operation(s) for reserved ips.
  name: Linode Reserved IPs API
  slug: linode-reserved-ips-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Add and manage locks on your Akamai Cloud resources to prevent you from inadvertently deleting them.
  name: Linode Resource locks API
  slug: linode-resource-locks-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to view information about available beta programs. You can sign up to participate in one of these programs using the [Enroll in a Beta program](https://techdocs.akamai.com/linode-
  name: Linode Review Beta programs API
  slug: linode-review-beta-programs-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View and configure security questions for your user account. Security questions can be used to help verify your identity when contacting Akamai Support.
  name: Linode Security questions API
  slug: linode-security-questions-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to manage transfer requests for specific Akamai Cloud Computing services. For example, you could request a service transfer to move a Linode from one region to another. Service tr
  name: Linode Service transfers API
  slug: linode-service-transfers-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Manage SSH keys for your user account. When creating a Linode, you can choose to have one or more SSH keys automatically added to the new Linode for secure access.
  name: Linode SSH keys API
  slug: linode-ssh-keys-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to open, view, and close support tickets, when you need assistance from Akamai.
  name: Linode Support tickets API
  slug: linode-support-tickets-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Templates API from Linode — 2 operation(s) for templates.
  name: Linode Templates API
  slug: linode-templates-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: View details about trusted devices associated with your user account. If needed, you can revoke a trusted device so any future login attempts from that device will go through the full authentication p
  name: Linode Trusted devices API
  slug: linode-trusted-devices-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Two-factor authentication (2FA) API from Linode — 4 operation(s) for two-factor authentication (2fa).
  name: Linode Two-factor authentication (2FA) API
  slug: linode-two-factor-authentication-2fa-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Users are individuals on your account that you set up to perform specific tasks. Use these operations to view and manage users, including giving them various levels of access to the services on your a
  name: Linode Users API
  slug: linode-users-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Managed Databases is Akamai's fully-managed, high-performance database service. Use these operations to create and manage clusters for Valkey engine databases.
  name: Linode Valkey API
  slug: linode-valkey-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The VLANs API from Linode — 2 operation(s) for vlans.
  name: Linode VLANs API
  slug: linode-vlans-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use these operations to review the available Block Storage volume types, including pricing.
  name: Linode Volume types API
  slug: linode-volume-types-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: Use the VPC subnet endpoints to view, create, and manage Virtual Private Cloud (VPC) subnet resources.
  name: Linode VPC subnets API
  slug: linode-vpc-subnets-api
- baseURL: https://api.linode.com/v4
  baseurl_source: declared
  description: The Rulesets API from Linode — 2 operation(s) for rulesets.
  name: Linode Rulesets API
  slug: linode-rulesets-api
artifact_total: 285
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Linode API v4 Account API
  slug: open-linode-account-api
- collection_type: open
  name: Linode API v4
  slug: open-linode-api-v4
- collection_type: open
  name: Linode API v4 Account Databases API
  slug: open-linode-databases-api
- collection_type: open
  name: Linode API v4 Account Domains API
  slug: open-linode-domains-api
- collection_type: open
  name: Linode API v4 Account Images API
  slug: open-linode-images-api
- collection_type: open
  name: Linode API v4 Account Linode Instances API
  slug: open-linode-linode-instances-api
- collection_type: open
  name: Linode API v4 Account Linode Kubernetes Engine (LKE) API
  slug: open-linode-linode-kubernetes-engine-lke-api
- collection_type: open
  name: Linode API v4 Account Longview API
  slug: open-linode-longview-api
- collection_type: open
  name: Linode API v4 Account Managed API
  slug: open-linode-managed-api
- collection_type: open
  name: Linode API v4 Account Networking API
  slug: open-linode-networking-api
- collection_type: open
  name: Linode API v4 Account NodeBalancers API
  slug: open-linode-nodebalancers-api
- collection_type: open
  name: Linode API v4 Account Object Storage API
  slug: open-linode-object-storage-api
- collection_type: open
  name: Linode API v4 Account Placement Groups API
  slug: open-linode-placement-groups-api
- collection_type: open
  name: Linode API v4 Account Profile API
  slug: open-linode-profile-api
- collection_type: open
  name: Linode API v4 Account Regions API
  slug: open-linode-regions-api
- collection_type: open
  name: Linode API v4 Account StackScripts API
  slug: open-linode-stackscripts-api
- collection_type: open
  name: Linode API v4 Account Support API
  slug: open-linode-support-api
- collection_type: open
  name: Linode API v4 Account Tags API
  slug: open-linode-tags-api
- collection_type: open
  name: Linode API v4 Account Volumes API
  slug: open-linode-volumes-api
- collection_type: open
  name: Linode API v4 Account VPCs API
  slug: open-linode-vpcs-api
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/agentic-access/linode-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/linode-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/security/linode-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/linode-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/authentication/linode-authentication.yml
  title: ''
  type: Authentication
  url: authentication/linode-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/scopes/linode-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/linode-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/linode
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/json-ld/linode-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/linode-context.jsonld
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/json-schema/linode-instance-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/linode-instance-schema.json
- group: company
  title: ''
  type: Website
  url: https://www.linode.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://techdocs.akamai.com/linode-api/reference/api
- group: docs
  title: ''
  type: Documentation
  url: https://techdocs.akamai.com/linode-api/
- group: docs
  title: ''
  type: APIReference
  url: https://techdocs.akamai.com/linode-api/reference/api
- group: start
  title: ''
  type: GettingStarted
  url: https://techdocs.akamai.com/linode-api/reference/get-started
- group: start
  title: ''
  type: SignUp
  url: https://login.linode.com/signup
- group: start
  title: ''
  type: Login
  url: https://login.linode.com/login
- group: start
  title: ''
  type: Console
  url: https://cloud.linode.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/linode
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/linode/linode-api-openapi
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/linode/linode-cli/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/linode/linode-api-openapi/blob/main/LICENSE
- group: operate
  title: ''
  type: StatusPage
  url: https://status.linode.com/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/packages/linode-packages.yml
  title: ''
  type: Packages
  url: packages/linode-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/packages/linode-packages.yml
  title: ''
  type: SDKs
  url: packages/linode-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/well-known/linode-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/linode-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/well-known/linode-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/linode-api-catalog.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/mcp/linode-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/linode-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/mcp/linode-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/linode-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/llms/linode-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/linode-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/conformance/linode-conformance.yml
  title: ''
  type: Conformance
  url: conformance/linode-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/errors/linode-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/linode-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/lifecycle/linode-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/linode-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/lifecycle/linode-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/linode-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/security/linode-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/linode-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/security/linode-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/linode-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/conventions/linode-conventions.yml
  title: ''
  type: Conventions
  url: conventions/linode-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/changelog/linode-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/linode-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/cli/linode-cli.yml
  title: ''
  type: CLI
  url: cli/linode-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/data-model/linode-data-model.yml
  title: ''
  type: DataModel
  url: data-model/linode-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/plans/linode-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/linode-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/rate-limits/linode-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/linode-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/finops/linode-finops.yml
  title: ''
  type: FinOps
  url: finops/linode-finops.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/vocabulary/linode-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/linode-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/json-structure/linode-structure.json
  title: ''
  type: JSONStructure
  url: json-structure/linode-structure.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/rules/linode-jsonschema-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/linode-jsonschema-spectral-rules.yml
created: '2026-05-04'
description: 'Linode — operating as Akamai Cloud since Akamai''s acquisition, with the Linode brand retained on the API, the CLI and the developer surface — is a cloud infrastructure provider offering virtual compute instances, GPU and accelerated plans, managed Kubernetes (LKE), S3-compatible Object Storage, Block Storage volumes, NodeBalancers, VPCs, Cloud Firewalls, managed MySQL/PostgreSQL/Valkey databases and DNS hosting. The Linode API v4 is a single cohesive REST surface at api.linode.com/v4 covering all of it: 358 paths and 539 operations in the first-party OpenAPI, documented at techdocs.akamai.com, with a generated CLI, first-party SDKs in Python, Go and TypeScript, a Terraform provider and an official read-only MCP server. Its price book is published as an unauthenticated API, so a stack can be costed with no account at all.'
features:
- Nanode 1 GB at $5/mo (smallest plan)
- Shared CPU 4 GB at $20/mo (most popular)
- Dedicated CPU 4 GB at $36/mo
- High Memory from $60/mo
- GPU (NVIDIA Blackwell) from ~$1.50/hr
- Distributed Compute Regions (200+ edge locations)
- Hourly billing capped at monthly rate
- 'API v4: 800 req/2-min default'
- 'Linode create/boot: 25 req/min'
- 'Object Storage (S3-compatible): $5/250 GB'
- 'NodeBalancer (load balancer): $10/mo'
- 'Backups: $2-$60/mo'
- 'Linode Kubernetes Engine (LKE): control plane free'
- Managed Databases (Postgres, MySQL, MongoDB)
- Personal access tokens (PATs)
- Now Akamai Cloud Computing (Linode brand retired)
finops:
- name: Linode Finops
  service_category: Cloud Compute
  slug: linode-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/linode.png
json_schemas:
- name: Account
  property_count: 14
  slug: linode-account
- name: Backup
  property_count: 8
  slug: linode-backup
- name: BackupResponse
  property_count: 2
  slug: linode-backupresponse
- name: Database
  property_count: 13
  slug: linode-database
- name: DatabaseRequest
  property_count: 2
  slug: linode-databaserequest
- name: Domain
  property_count: 13
  slug: linode-domain
- name: DomainRecord
  property_count: 9
  slug: linode-domainrecord
- name: DomainRecordRequest
  property_count: 7
  slug: linode-domainrecordrequest
- name: DomainRequest
  property_count: 5
  slug: linode-domainrequest
- name: Event
  property_count: 9
  slug: linode-event
- name: Firewall
  property_count: 7
  slug: linode-firewall
- name: FirewallRequest
  property_count: 3
  slug: linode-firewallrequest
- name: FirewallRule
  property_count: 6
  slug: linode-firewallrule
- name: FirewallUpdateRequest
  property_count: 3
  slug: linode-firewallupdaterequest
- name: Image
  property_count: 11
  slug: linode-image
- name: ImageRequest
  property_count: 3
  slug: linode-imagerequest
- name: ImageUpdateRequest
  property_count: 2
  slug: linode-imageupdaterequest
- name: Linode Instance
  property_count: 16
  slug: linode-instance
- name: Invoice
  property_count: 6
  slug: linode-invoice
- name: IPAddress
  property_count: 9
  slug: linode-ipaddress
- name: IPv6Address
  property_count: 5
  slug: linode-ipv6address
- name: IPv6Range
  property_count: 3
  slug: linode-ipv6range
- name: KubernetesVersion
  property_count: 1
  slug: linode-kubernetesversion
- name: Linode
  property_count: 17
  slug: linode-linode
- name: LinodeIPAddresses
  property_count: 2
  slug: linode-linodeipaddresses
- name: LinodeRebuildRequest
  property_count: 7
  slug: linode-linoderebuildrequest
- name: LinodeRequest
  property_count: 14
  slug: linode-linoderequest
- name: LinodeUpdateRequest
  property_count: 4
  slug: linode-linodeupdaterequest
- name: LKECluster
  property_count: 9
  slug: linode-lkecluster
- name: LKEClusterRequest
  property_count: 6
  slug: linode-lkeclusterrequest
- name: LKEClusterUpdateRequest
  property_count: 4
  slug: linode-lkeclusterupdaterequest
- name: LongviewClient
  property_count: 7
  slug: linode-longviewclient
- name: LongviewClientRequest
  property_count: 1
  slug: linode-longviewclientrequest
- name: ManagedService
  property_count: 13
  slug: linode-managedservice
- name: ManagedServiceRequest
  property_count: 8
  slug: linode-managedservicerequest
- name: NodeBalancer
  property_count: 11
  slug: linode-nodebalancer
- name: NodeBalancerRequest
  property_count: 4
  slug: linode-nodebalancerrequest
- name: NodeBalancerUpdateRequest
  property_count: 3
  slug: linode-nodebalancerupdaterequest
- name: NodePool
  property_count: 5
  slug: linode-nodepool
- name: NodePoolRequest
  property_count: 3
  slug: linode-nodepoolrequest
- name: ObjectStorageBucket
  property_count: 6
  slug: linode-objectstoragebucket
- name: ObjectStorageEndpointList
  property_count: 1
  slug: linode-objectstorageendpointlist
- name: ObjectStorageKey
  property_count: 6
  slug: linode-objectstoragekey
- name: ObjectStorageKeyRequest
  property_count: 2
  slug: linode-objectstoragekeyrequest
- name: PaginatedConfigList
  property_count: 0
  slug: linode-paginatedconfiglist
- name: PaginatedDatabaseEngineList
  property_count: 0
  slug: linode-paginateddatabaseenginelist
- name: PaginatedDatabaseList
  property_count: 0
  slug: linode-paginateddatabaselist
- name: PaginatedDatabaseTypeList
  property_count: 0
  slug: linode-paginateddatabasetypelist
- name: PaginatedDiskList
  property_count: 0
  slug: linode-paginateddisklist
- name: PaginatedDomainList
  property_count: 0
  slug: linode-paginateddomainlist
- name: PaginatedDomainRecordList
  property_count: 0
  slug: linode-paginateddomainrecordlist
- name: PaginatedEventList
  property_count: 0
  slug: linode-paginatedeventlist
- name: PaginatedFirewallList
  property_count: 0
  slug: linode-paginatedfirewalllist
- name: PaginatedImageList
  property_count: 0
  slug: linode-paginatedimagelist
- name: PaginatedInvoiceList
  property_count: 0
  slug: linode-paginatedinvoicelist
- name: PaginatedIPAddressList
  property_count: 0
  slug: linode-paginatedipaddresslist
- name: PaginatedKernelList
  property_count: 0
  slug: linode-paginatedkernellist
- name: PaginatedLinodeList
  property_count: 0
  slug: linode-paginatedlinodelist
- name: PaginatedLinodeTypeList
  property_count: 0
  slug: linode-paginatedlinodetypelist
- name: PaginatedLKEClusterList
  property_count: 0
  slug: linode-paginatedlkeclusterlist
- name: PaginatedLongviewClientList
  property_count: 0
  slug: linode-paginatedlongviewclientlist
- name: PaginatedManagedContactList
  property_count: 0
  slug: linode-paginatedmanagedcontactlist
- name: PaginatedManagedIssueList
  property_count: 0
  slug: linode-paginatedmanagedissuelist
- name: PaginatedManagedServiceList
  property_count: 0
  slug: linode-paginatedmanagedservicelist
- name: PaginatedNodeBalancerConfigList
  property_count: 0
  slug: linode-paginatednodebalancerconfiglist
- name: PaginatedNodeBalancerList
  property_count: 0
  slug: linode-paginatednodebalancerlist
- name: PaginatedNodePoolList
  property_count: 0
  slug: linode-paginatednodepoollist
- name: PaginatedObjectStorageBucketList
  property_count: 0
  slug: linode-paginatedobjectstoragebucketlist
- name: PaginatedObjectStorageKeyList
  property_count: 0
  slug: linode-paginatedobjectstoragekeylist
- name: PaginatedPaymentList
  property_count: 0
  slug: linode-paginatedpaymentlist
- name: PaginatedPlacementGroupList
  property_count: 0
  slug: linode-paginatedplacementgrouplist
- name: PaginatedRegionList
  property_count: 0
  slug: linode-paginatedregionlist
- name: PaginatedSSHKeyList
  property_count: 0
  slug: linode-paginatedsshkeylist
- name: PaginatedStackScriptList
  property_count: 0
  slug: linode-paginatedstackscriptlist
- name: PaginatedSubnetList
  property_count: 0
  slug: linode-paginatedsubnetlist
- name: PaginatedSupportTicketList
  property_count: 0
  slug: linode-paginatedsupportticketlist
- name: PaginatedTagList
  property_count: 0
  slug: linode-paginatedtaglist
- name: PaginatedTokenList
  property_count: 0
  slug: linode-paginatedtokenlist
- name: PaginatedUserList
  property_count: 0
  slug: linode-paginateduserlist
- name: PaginatedVLANList
  property_count: 0
  slug: linode-paginatedvlanlist
- name: PaginatedVolumeList
  property_count: 0
  slug: linode-paginatedvolumelist
- name: PaginatedVPCList
  property_count: 0
  slug: linode-paginatedvpclist
- name: Pagination
  property_count: 3
  slug: linode-pagination
- name: Payment
  property_count: 3
  slug: linode-payment
- name: PaymentRequest
  property_count: 1
  slug: linode-paymentrequest
- name: PlacementGroup
  property_count: 7
  slug: linode-placementgroup
- name: PlacementGroupRequest
  property_count: 4
  slug: linode-placementgrouprequest
- name: Profile
  property_count: 8
  slug: linode-profile
- name: Region
  property_count: 7
  slug: linode-region
- name: SSHKey
  property_count: 4
  slug: linode-sshkey
- name: SSHKeyRequest
  property_count: 2
  slug: linode-sshkeyrequest
- name: StackScript
  property_count: 12
  slug: linode-stackscript
- name: StackScriptRequest
  property_count: 6
  slug: linode-stackscriptrequest
- name: Subnet
  property_count: 6
  slug: linode-subnet
- name: SubnetRequest
  property_count: 2
  slug: linode-subnetrequest
- name: SupportTicket
  property_count: 8
  slug: linode-supportticket
- name: SupportTicketRequest
  property_count: 8
  slug: linode-supportticketrequest
- name: Tag
  property_count: 1
  slug: linode-tag
- name: TagRequest
  property_count: 5
  slug: linode-tagrequest
- name: Token
  property_count: 6
  slug: linode-token
- name: TokenRequest
  property_count: 3
  slug: linode-tokenrequest
- name: User
  property_count: 5
  slug: linode-user
- name: UserRequest
  property_count: 3
  slug: linode-userrequest
- name: Volume
  property_count: 11
  slug: linode-volume
- name: VolumeRequest
  property_count: 5
  slug: linode-volumerequest
- name: VolumeUpdateRequest
  property_count: 2
  slug: linode-volumeupdaterequest
- name: VPC
  property_count: 7
  slug: linode-vpc
- name: VPCRequest
  property_count: 4
  slug: linode-vpcrequest
- name: VPCUpdateRequest
  property_count: 2
  slug: linode-vpcupdaterequest
json_structures:
- name: Linode Structure
  property_count: 0
  slug: linode-structure
jsonld:
- class_count: 0
  name: Linode Context
  property_count: 12
  slug: linode-context
layout: provider
mcp_servers:
- description: Akamai publishes one official Model Context Protocol server for Akamai Cloud — the product formerly and still widely known as Linode — at akamai-developers/akamai-cloud-mcp. It is read-only by constru
  name: Akamai Cloud MCP Server
  slug: akamai-cloud-mcp-server
modified: '2026-09-17'
name: Linode
nav: Providers
network: true
overview: 'Linode publishes 127 APIs on the [APIs.io](https://apis.io/) network, including Account API, Databases API, Domains API, and 124 more. Tagged areas include Cloud Computing, Infrastructure-as-a-Service, Virtual Machines, Kubernetes, and Object Storage.


  The Linode catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Linode''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, developer console, changelog, and 37 more developer resources.'
plans:
- name: Linode Plans Pricing
  plan_count: 7
  slug: linode-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 12
  name: Linode Rate Limits
  slug: linode-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Linode API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: linode-jsonschema-spectral-rules
scopes:
- name: Linode Scopes
  scope_count: 30
  slug: linode-scopes
  summary_line: 30 scopes · authorizationCode
score:
  band: strong
  composite: 55.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 79.8
    catalog_earned_first_party: 24.0
    catalog_gap: 35.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 52.6
    contract_governance: 28.0
    contract_quality: 58.1
    developer_ergonomics: 28.0
    discoverability: 71.7
    operational_transparency: 84.2
  previous_composite: 55.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 123
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.4
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/linode/refs/heads/main/screenshots/linode-2026-06-20T184550.png
security:
- kind: authentication
  name: Linode Authentication
  slug: linode-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Linode Domain Security
  slug: linode-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Linode Vulnerability Disclosure
  slug: linode-vulnerability-disclosure
  summary_line: Hackerone
slug: linode
tags:
- Cloud Computing
- Infrastructure-as-a-Service
- Virtual Machines
- Kubernetes
- Object Storage
- Block Storage
- DNS
- Managed Database
- Networking
- GPU
- Load Balancer
- Developer Tools
website: https://www.linode.com/
---
