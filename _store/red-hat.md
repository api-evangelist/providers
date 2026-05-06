---
aid: red-hat
name: Red Hat
description: APIs and developer resources from Red Hat, a leading provider of enterprise open source solutions including Linux, cloud, container, and Kubernetes technologies.
type: Index
image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
url: https://raw.githubusercontent.com/api-evangelist/red-hat/refs/heads/main/apis.yml
created: '2024-01-15'
modified: '2026-04-18'
specificationVersion: '0.19'
tags:
  - Cloud
  - Containers
  - Enterprise
  - Hybrid Cloud
  - Kubernetes
  - Linux
  - Open Source
apis:
  - name: Red Hat OpenShift API
    description: RESTful API for managing OpenShift clusters, applications, and resources on Red Hat's enterprise Kubernetes platform.
    image: https://www.redhat.com/cms/managed-files/openshift-logo.png
    humanUrl: https://docs.openshift.com/container-platform/latest/rest_api/index.html
    baseUrl: https://api.openshift.com
    tags:
      - Cloud Native
      - Containers
      - Kubernetes
      - Platform as a Service
    properties:
      - type: Documentation
        url: https://docs.openshift.com/container-platform/latest/rest_api/index.html
      - type: OpenAPI
        url: https://api.openshift.com/api/clusters_mgmt/v1/openapi
      - type: Authentication
        url: https://docs.openshift.com/container-platform/latest/authentication/index.html
      - type: GettingStarted
        url: https://docs.openshift.com/container-platform/latest/getting_started/openshift-overview.html
      - type: ChangeLog
        url: https://docs.openshift.com/container-platform/latest/release_notes/ocp-4-release-notes.html
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat OpenShift Cluster Manager API
    description: API for provisioning, managing, and monitoring OpenShift clusters across cloud providers through the Red Hat Hybrid Cloud Console. Supports cluster lifecycle operations including creation, scaling, and upgrades.
    image: https://www.redhat.com/cms/managed-files/openshift-logo.png
    humanUrl: https://api.openshift.com/
    baseUrl: https://api.openshift.com
    tags:
      - Cluster Management
      - Hybrid Cloud
      - Kubernetes
      - Provisioning
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest/html/managing_clusters/assembly-managing-clusters
      - type: OpenAPI
        url: https://api.openshift.com/api/clusters_mgmt/v1/openapi
      - type: OpenAPI
        url: openapi/red-hat-openshift-cluster-manager-openapi.yml
      - type: GettingStarted
        url: https://access.redhat.com/articles/6114701
      - type: GitHubRepository
        url: https://github.com/openshift-online/ocm-api-model
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Ansible Automation Platform API
    description: API for automating IT infrastructure, application deployment, and configuration management through Ansible.
    humanUrl: https://docs.ansible.com/ansible-tower/latest/html/towerapi/index.html
    baseUrl: https://ansible-platform.example.com/api/v2
    tags:
      - Automation
      - Configuration Management
      - DevOps
      - Infrastructure as Code
    properties:
      - type: Documentation
        url: https://docs.ansible.com/ansible-tower/latest/html/towerapi/index.html
      - type: APIReference
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/api_ref.html
      - type: Authentication
        url: https://docs.ansible.com/automation-controller/latest/html/controllerapi/authentication.html
      - type: GettingStarted
        url: https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.6
      - type: OpenAPI
        url: openapi/red-hat-ansible-automation-platform-openapi.yml
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Quay API
    description: Container registry API for storing, distributing, and securing container images.
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_quay/
    baseUrl: https://quay.io/api/v1
    tags:
      - Container Registry
      - Docker
      - Image Management
      - Security
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_quay/
      - type: APIReference
        url: https://docs.redhat.com/en/documentation/red_hat_quay/latest/html-single/red_hat_quay_api_guide/index
      - type: OpenAPI
        url: https://quay.io/api/v1/discovery
      - type: OpenAPI
        url: openapi/red-hat-quay-openapi.yml
      - type: GitHubRepository
        url: https://github.com/quay/quay
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Insights API
    description: Predictive analytics and remediation API for proactive identification and resolution of infrastructure issues.
    humanUrl: https://console.redhat.com/docs/api
    baseUrl: https://console.redhat.com/api
    tags:
      - Analytics
      - Compliance
      - Monitoring
      - Security
    properties:
      - type: Documentation
        url: https://console.redhat.com/docs/api
      - type: Console
        url: https://console.redhat.com/api/api-docs
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
      - type: GettingStarted
        url: https://docs.redhat.com/en/documentation/red_hat_insights/1-latest/html/using_the_red_hat_insights_api/making-api-calls
      - type: OpenAPI
        url: openapi/red-hat-insights-openapi.yml
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Subscription Management API
    description: API for managing Red Hat subscriptions, entitlements, and system registrations.
    humanUrl: https://access.redhat.com/management/api
    baseUrl: https://api.access.redhat.com/management/v1
    tags:
      - Entitlements
      - Licensing
      - Subscriptions
      - System Management
    properties:
      - type: Documentation
        url: https://access.redhat.com/management/api
      - type: APIReference
        url: https://access.redhat.com/management/api/rhsm
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Satellite API
    description: REST API for managing Red Hat Satellite infrastructure, including content management, provisioning, configuration, and patch management across large-scale Linux environments.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/using_the_satellite_rest_api/index
    baseUrl: https://satellite.example.com/api/v2
    tags:
      - Content Management
      - Patch Management
      - Provisioning
      - Systems Management
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_satellite/6.16/html-single/using_the_satellite_rest_api/index
      - type: OpenAPI
        url: openapi/red-hat-satellite-openapi.yml
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Advanced Cluster Management API
    description: API for managing multiple Kubernetes clusters across hybrid cloud environments, providing cluster lifecycle management, policy-based governance, and application deployment.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15
    baseUrl: https://multicloud-console.example.com/api
    tags:
      - Cluster Management
      - Governance
      - Kubernetes
      - Multi-Cluster
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.15
      - type: GitHubRepository
        url: https://github.com/stolostron/rhacm-docs
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Advanced Cluster Security API
    description: REST API for managing Kubernetes-native security including vulnerability management, compliance, network segmentation, and risk profiling across OpenShift and Kubernetes clusters.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_security_for_kubernetes/4.5
    baseUrl: https://central.example.com/v1
    tags:
      - Compliance
      - Kubernetes
      - Security
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_security_for_kubernetes/4.5
      - type: APIReference
        url: https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_security_for_kubernetes/4.5
      - type: GitHubRepository
        url: https://github.com/stackrox/stackrox
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Build of Keycloak Admin REST API
    description: Admin REST API for managing authentication, authorization, identity brokering, and user federation in the Red Hat build of Keycloak identity and access management platform.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_developer_guide/admin_rest_api
    baseUrl: https://keycloak.example.com/admin/realms
    tags:
      - Authentication
      - Authorization
      - Identity
      - Single Sign-On
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0/html/server_developer_guide/admin_rest_api
      - type: GettingStarted
        url: https://docs.redhat.com/en/documentation/red_hat_build_of_keycloak/26.0
      - type: OpenAPI
        url: openapi/red-hat-keycloak-admin-openapi.yml
      - type: GitHubRepository
        url: https://github.com/keycloak/keycloak
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat 3scale API Management
    description: API management platform providing access control, rate limiting, analytics, and developer portal capabilities for managing the full lifecycle of APIs.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_3scale_api_management/2.15
    baseUrl: https://3scale-admin.example.com/admin/api
    tags:
      - API Gateway
      - API Management
      - Developer Portal
      - Rate Limiting
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_3scale_api_management/2.15
      - type: GettingStarted
        url: https://developers.redhat.com/products/3scale/getting-started
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Cost Management API
    description: API for tracking and analyzing costs associated with Red Hat OpenShift clusters and cloud infrastructure, providing visibility into resource consumption and spend.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog/api/cost-management
    baseUrl: https://console.redhat.com/api/cost-management/v1
    tags:
      - Analytics
      - Cloud
      - Cost Management
      - FinOps
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog/api/cost-management
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Image Builder API
    description: API for building customized RHEL system images for deployment across cloud providers, virtualization platforms, and bare metal environments through the Hybrid Cloud Console.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog/api/image-builder
    baseUrl: https://console.redhat.com/api/image-builder/v1
    tags:
      - Cloud
      - Image Building
      - Provisioning
      - RHEL
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog/api/image-builder
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Vulnerability Management API
    description: API for assessing and monitoring security vulnerabilities across RHEL systems, providing CVE tracking, severity scoring, and remediation guidance.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog/api/vulnerability
    baseUrl: https://console.redhat.com/api/vulnerability/v1
    tags:
      - Compliance
      - CVE
      - Security
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog/api/vulnerability
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Patch API
    description: API for managing and applying patches to RHEL systems, providing advisories, package updates, and system patch status through the Hybrid Cloud Console.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/patch/v3
    tags:
      - Patch Management
      - RHEL
      - Security
      - Updates
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Compliance API
    description: API for managing security policy compliance assessments on RHEL systems using SCAP profiles, providing compliance scoring, reporting, and policy management.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/compliance/v2
    tags:
      - Compliance
      - Policy Management
      - SCAP
      - Security
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Build of Apicurio Registry API
    description: REST API for managing schemas and API design artifacts in a schema registry, supporting formats including Avro, JSON Schema, Protobuf, OpenAPI, and AsyncAPI.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.0
    baseUrl: https://registry.example.com/apis/registry/v2
    tags:
      - API Design
      - Data Governance
      - Event-Driven
      - Schema Registry
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/3.0
      - type: GettingStarted
        url: https://docs.redhat.com/en/documentation/red_hat_build_of_apicurio_registry/2.5/html-single/apicurio_registry_user_guide/index
      - type: Website
        url: https://www.apicur.io/registry/
      - type: GitHubRepository
        url: https://github.com/Apicurio/apicurio-registry
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Streams for Apache Kafka Bridge API
    description: HTTP bridge API for producing and consuming messages to Apache Kafka topics without requiring a native Kafka client, deployed as part of Red Hat Streams for Apache Kafka on OpenShift.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_streams_for_apache_kafka/3.1
    baseUrl: https://kafka-bridge.example.com
    tags:
      - Data Integration
      - Event Streaming
      - Kafka
      - Messaging
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_streams_for_apache_kafka/3.1
      - type: GettingStarted
        url: https://developers.redhat.com/products/streams-for-apache-kafka/getting-started
      - type: AsyncAPI
        url: asyncapi/red-hat-kafka-bridge-asyncapi.yml
      - type: GitHubRepository
        url: https://github.com/strimzi/strimzi-kafka-operator
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Ansible Lightspeed API
    description: AI-powered API that provides generative AI assistance for creating Ansible automation content, helping users generate Ansible Playbooks and task recommendations.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/ansible-wisdom
    tags:
      - Ansible
      - Artificial Intelligence
      - Automation
      - Generative AI
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Managed Inventory API
    description: REST API for managing host inventory data within the Hybrid Cloud Console, providing system profile information, tagging, grouping, and host lifecycle management.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/inventory/v1
    tags:
      - Host Management
      - Inventory
      - RHEL
      - Systems Management
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Remediations API
    description: API for creating and managing automated remediation playbooks that address security vulnerabilities, compliance issues, and configuration drift identified by Red Hat Insights services.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/remediations/v1
    tags:
      - Automation
      - Compliance
      - Remediation
      - Security
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Notifications API
    description: API for managing notification preferences, integrations, and event routing within the Hybrid Cloud Console, enabling alerts through email, webhook, and third-party services.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/notifications/v1
    tags:
      - Alerts
      - Integrations
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
      - type: AsyncAPI
        url: asyncapi/red-hat-notifications-webhooks-asyncapi.yml
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Role-Based Access Control API
    description: API for managing role-based access control policies within the Hybrid Cloud Console, including user groups, roles, permissions, and access policies.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/rbac/v1
    tags:
      - Access Control
      - Authorization
      - Identity
      - Security
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Advisor API
    description: Predictive analytics API that provides proactive recommendations for improving the stability, performance, and security of RHEL systems through the Hybrid Cloud Console.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/insights/v1
    tags:
      - Analytics
      - Monitoring
      - Recommendations
      - RHEL
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Malware Detection API
    description: API for detecting potential malware signatures on RHEL systems registered with the Hybrid Cloud Console, providing scanning results and threat analysis.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/malware-detection/v1
    tags:
      - Malware
      - RHEL
      - Security
      - Threat Detection
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Sources API
    description: API for managing source connections and integrations within the Hybrid Cloud Console, enabling connectivity to cloud providers and other external services.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/sources/v3.1
    tags:
      - Cloud
      - Configuration
      - Data Sources
      - Integrations
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Integrations API
    description: API for configuring third-party integrations and notification endpoints within the Hybrid Cloud Console, supporting webhook, email, and service integrations.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/integrations/v1
    tags:
      - Configuration
      - Integrations
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Resource Optimization API
    description: API for analyzing resource utilization and providing optimization recommendations for RHEL systems, helping right-size workloads and reduce waste.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/ros/v1
    tags:
      - Analytics
      - FinOps
      - Resource Optimization
      - RHEL
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Export Service API
    description: API for exporting data from Hybrid Cloud Console services in JSON or CSV formats, enabling bulk data retrieval for inventory, notifications, and other services.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/export/v1
    tags:
      - Automation
      - Data Export
      - Inventory
      - Reporting
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Playbook Dispatcher API
    description: API for dispatching and managing Ansible Playbook execution on hosts connected via Cloud Connector, enabling automated remediation and configuration management.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/playbook-dispatcher/v1
    tags:
      - Ansible
      - Automation
      - Playbooks
      - Remediation
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Content Sources API
    description: API for managing custom and Red Hat content repositories within the Hybrid Cloud Console, enabling organizations to curate and distribute software packages.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/content-sources/v1
    tags:
      - Content Management
      - Packages
      - Repositories
      - RHEL
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Tasks API
    description: API for managing and issuing Red Hat-generated tasks on registered infrastructure, enabling automated system maintenance and configuration operations.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/tasks/v1
    tags:
      - Automation
      - RHEL
      - Systems Management
      - Task Management
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Subscriptions Usage API
    description: API for monitoring and reporting Red Hat subscription utilization including OpenShift, RHEL, and other product usage metrics for capacity planning and compliance.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/rhsm-subscriptions/v1
    tags:
      - Compliance
      - Reporting
      - Subscriptions
      - Usage
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Assisted Installer API
    description: REST API for the OpenShift Assisted Installer service, enabling automated discovery, validation, and installation of OpenShift clusters across bare metal, vSphere, and other platforms.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/installing-with-api
    baseUrl: https://api.openshift.com/api/assisted-install/v2
    tags:
      - Bare Metal
      - Cluster Provisioning
      - Installation
      - OpenShift
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025/html/installing_openshift_container_platform_with_the_assisted_installer/installing-with-api
      - type: OpenAPI
        url: https://api.openshift.com/api/assisted-install/v2/openapi
      - type: GitHubRepository
        url: https://github.com/openshift/assisted-service
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Account Management Service API
    description: API for managing user subscriptions, clusters, and organizations through the OpenShift Cluster Manager, providing account-level operations and resource management.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://api.openshift.com/api/accounts_mgmt/v1
    tags:
      - Account Management
      - OpenShift
      - Organizations
      - Subscriptions
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Authorization Service API
    description: API for managing access control on resources of OpenShift Cluster Manager services, enabling fine-grained authorization policies and permission management.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://api.openshift.com/api/authorizations/v1
    tags:
      - Access Control
      - Authorization
      - OpenShift
      - Security
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Service Logs API
    description: API for receiving and maintaining logs from internal sources related to OpenShift clusters, providing centralized log management and retrieval.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://api.openshift.com/api/service_logs/v1
    tags:
      - Logging
      - Monitoring
      - Observability
      - OpenShift
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Connector Management API
    description: REST API for managing connectors that enable integration between Red Hat services and external systems, supporting connector lifecycle operations.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://api.openshift.com/api/connector_mgmt/v1
    tags:
      - Connectors
      - Data Integration
      - Integrations
      - OpenShift
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Upgrades Information Service API
    description: API for retrieving upgrade path information and recommendations for OpenShift clusters, helping plan and execute cluster version upgrades safely.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://api.openshift.com/api/upgrades_info/v1
    tags:
      - Cluster Management
      - OpenShift
      - Upgrades
      - Version Management
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Automation Hub API
    description: API for fetching, uploading, organizing, and distributing Ansible Collections through Red Hat Automation Hub, providing access to Red Hat Certified and partner content.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/automation-hub/
    tags:
      - Ansible
      - Automation
      - Collections
      - Content Management
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: GettingStarted
        url: https://docs.redhat.com/en/documentation/red_hat_ansible_automation_platform/2.4/html-single/getting_started_with_automation_hub/index
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Operator Gathering Conditions Service API
    description: API providing gathering conditions to the Insights Operator, defining what data should be collected from OpenShift clusters for analysis and recommendations.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/gathering/v1
    tags:
      - Data Collection
      - Insights
      - OpenShift
      - Operators
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Payload Ingress Service API
    description: API for ingesting payloads and data uploads from registered systems into the Hybrid Cloud Console platform for processing by downstream services.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/ingress/v1
    tags:
      - Data Ingestion
      - Platform
      - Systems Management
      - Upload
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Lightspeed Advisor for OpenShift API
    description: Aggregation API for Insights Advisor that exposes recommendations for single and multiple OpenShift clusters, providing AI-powered operational guidance.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/insights-results-aggregator/v2
    tags:
      - Artificial Intelligence
      - Monitoring
      - OpenShift
      - Recommendations
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat OCP Vulnerability Dashboard API
    description: API for tracking and analyzing vulnerabilities affecting OpenShift Container Platform clusters, providing CVE exposure data and remediation status.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/ocp-vulnerability/v1
    tags:
      - CVE
      - OpenShift
      - Security
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Web-RCA Service API
    description: API for the Web Root Cause Analysis service, providing incident tracking, root cause analysis, and post-incident review capabilities for OpenShift managed services.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://api.openshift.com/api/web-rca/v1
    tags:
      - Incident Management
      - OpenShift
      - Operations
      - Root Cause Analysis
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Case Management API
    description: API for managing support cases through the Red Hat Customer Portal, supporting case creation, updates, comments, attachments, and escalation workflows.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://api.access.redhat.com/support/v1
    tags:
      - Case Management
      - Customer Portal
      - Incident Management
      - Support
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Security Data API
    description: Public API for querying Red Hat security data including CVE details, CSAF advisories, OVAL data, and vulnerability severity scores across Red Hat products.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_security_data_api/1.0/html-single/red_hat_security_data_api/index
    baseUrl: https://access.redhat.com/hydra/rest/securitydata
    tags:
      - CSAF
      - CVE
      - Security
      - Vulnerability Management
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_security_data_api/1.0/html-single/red_hat_security_data_api/index
      - type: GitHubRepository
        url: https://github.com/RedHatOfficial/rhsecapi
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Edge Management API
    description: API for fleet edge management capabilities including device provisioning, image management, update orchestration, and fleet-level configuration of RHEL-based edge devices.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://docs.redhat.com/en/documentation/red_hat_edge_manager/1.0/html/architecture/red_hat_edge_manager_architecture
    baseUrl: https://console.redhat.com/api/edge/v1
    tags:
      - Device Management
      - Edge Computing
      - Fleet Management
      - IoT
    properties:
      - type: Documentation
        url: https://docs.redhat.com/en/documentation/red_hat_edge_manager/1.0/html/architecture/red_hat_edge_manager_architecture
      - type: GitHubRepository
        url: https://github.com/RedHatInsights/edge-api
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
  - name: Red Hat Lightspeed for RHEL Planning API
    description: API providing RHEL product lifecycle data including release dates, end-of-life schedules, and upgrade path planning information.
    image: https://www.redhat.com/cms/managed-files/Logo-Red_Hat-A-Standard-RGB.svg
    humanUrl: https://developers.redhat.com/api-catalog
    baseUrl: https://console.redhat.com/api/roadmap/v1
    tags:
      - Lifecycle
      - Planning
      - Product Roadmap
      - RHEL
    properties:
      - type: Documentation
        url: https://developers.redhat.com/api-catalog
      - type: Authentication
        url: https://access.redhat.com/articles/3626371
    contact:
      - type: Support
        url: https://access.redhat.com/support
common:
  - type: JSONLD
    url: json-ld/red-hat-context.jsonld
  - type: JSONSchema
    url: json-schema/red-hat-openshift-cluster-schema.json
  - type: JSONSchema
    url: json-schema/red-hat-ansible-job-schema.json
  - type: JSONSchema
    url: json-schema/red-hat-insights-advisory-schema.json
  - type: JSONSchema
    url: json-schema/red-hat-quay-repository-schema.json
  - type: Features
    url: https://www.redhat.com/en/technologies
  - type: UseCases
    url: https://www.redhat.com/en/solutions
  - type: Integrations
    url: https://catalog.redhat.com
  - type: Portal
    url: https://developers.redhat.com
  - type: GettingStarted
    url: https://developers.redhat.com/get-started
  - type: Documentation
    url: https://docs.redhat.com/en/products
  - type: Blog
    url: https://developers.redhat.com/blog
  - type: Support
    url: https://access.redhat.com/support
  - type: StatusPage
    url: https://status.redhat.com
  - type: TermsOfService
    url: https://www.redhat.com/en/about/terms-use
  - type: PrivacyPolicy
    url: https://www.redhat.com/en/about/privacy-policy
  - type: Authentication
    url: https://access.redhat.com/articles/3626371
  - type: Console
    url: https://console.redhat.com
  - type: Website
    url: https://www.redhat.com
  - type: SignUp
    url: https://developers.redhat.com/register
  - type: Login
    url: https://sso.redhat.com
  - type: GitHubOrganization
    url: https://github.com/redhatofficial
  - type: SDK
    url: https://github.com/openshift/client-go
  - type: CLI
    url: https://docs.openshift.com/container-platform/latest/cli_reference/openshift_cli/getting-started-cli.html
  - type: GitHubRepository
    url: https://github.com/redhat-developer
  - type: Community
    url: https://access.redhat.com/discussions
  - type: StackOverflow
    url: https://developers.redhat.com/stack-overflow
  - type: YouTube
    url: https://developers.redhat.com/videos
  - type: Security
    url: https://access.redhat.com/security/vulnerabilities
  - type: API Catalog
    url: https://developers.redhat.com/api-catalog
  - type: KnowledgeCenter
    url: https://access.redhat.com/knowledgebase
  - type: Training
    url: https://www.redhat.com/en/services/training-and-certification
  - type: Events
    url: https://www.redhat.com/en/events
  - type: X
    url: https://twitter.com/RedHat
  - type: LinkedIn
    url: https://www.linkedin.com/company/red-hat
  - type: Feed
    url: https://developers.redhat.com/blog/feed
  - type: Security Data
    url: https://access.redhat.com/security/data
  - type: Ecosystem Catalog
    url: https://catalog.redhat.com
  - type: Product Lifecycle
    url: https://access.redhat.com/product-life-cycles
  - type: Customer Portal
    url: https://access.redhat.com
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
