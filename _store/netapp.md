---
aid: netapp
url: https://raw.githubusercontent.com/api-evangelist/netapp/refs/heads/main/apis.yml
apis:
- name: NetApp Cloud Manager API
  description: API for managing NetApp Cloud Volumes ONTAP and cloud data services.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://cloudmanager.cloud.netapp.com
  humanURL: https://docs.netapp.com/us-en/cloud-manager-automation/
  tags:
  - Automation
  - Cloud Management
  - ONTAP
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/cloud-manager-automation/
  - type: OpenAPI
    url: https://docs.netapp.com/us-en/cloud-manager-automation/api/openapi.yaml
  - type: Authentication
    url: https://docs.netapp.com/us-en/cloud-manager-automation/platform/get_identifiers.html
  - type: Getting Started
    url: https://docs.netapp.com/us-en/cloud-manager-automation/cm/your_api_call.html
  - type: Cloud Volumes ONTAP Overview
    url: https://docs.netapp.com/us-en/cloud-manager-automation/cm/overview.html
- name: NetApp ONTAP REST API
  description: REST API for NetApp ONTAP storage management system.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<cluster-management-ip>/api
  humanURL: https://docs.netapp.com/us-en/ontap-automation/
  tags:
  - ONTAP
  - REST API
  - Storage Management
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/ontap-automation/
  - type: Reference
    url: https://docs.netapp.com/us-en/ontap-automation/reference/api_reference.html
  - type: Getting Started
    url: https://docs.netapp.com/us-en/ontap-automation/getting_started_with_the_ontap_rest_api.html
  - type: Authentication
    url: https://docs.netapp.com/us-en/ontap-automation/rest/authentication.html
  - type: What's New
    url: https://docs.netapp.com/us-en/ontap-automation/whats-new.html
  - type: REST API Reference (ONTAP 9.18.1)
    url: https://docs.netapp.com/us-en/ontap-restapi/
  - type: Access REST API
    url: https://docs.netapp.com/us-en/ontap-automation/get-started/access_rest_api.html
  - type: GitHub
    url: https://github.com/NetApp/ontap-rest-python
  - type: DevNet
    url: https://devnet.netapp.com/restapi.php
  - type: OpenAPI
    url: openapi/netapp-ontap-openapi.yml
  - type: JSONSchema
    url: json-schema/netapp-volume-schema.json
  - type: JSONLDContext
    url: json-ld/netapp-context.jsonld
- name: NetApp Cloud Volumes Service API
  description: API for managing NetApp Cloud Volumes Service in major cloud providers.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://cloudvolumesgcp-api.netapp.com
  humanURL: https://cloud.google.com/architecture/partners/netapp-cloud-volumes/api
  tags:
  - AWS
  - Azure
  - Cloud Volumes
  - GCP
  properties:
  - type: Documentation
    url: https://cloud.google.com/architecture/partners/netapp-cloud-volumes/api
  - type: API Reference
    url: https://cloud.google.com/architecture/partners/netapp-cloud-volumes/reference
  - type: Google Cloud NetApp Volumes REST Reference
    url: https://docs.cloud.google.com/netapp/volumes/docs/reference/rest
  - type: APIs and Reference
    url: https://cloud.google.com/netapp/volumes/docs/apis
- name: NetApp Astra Control API
  description: API for Kubernetes-native application data management.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://astra.netapp.io/accounts
  humanURL: https://docs.netapp.com/us-en/astra-automation/
  tags:
  - Application Management
  - Container Storage
  - Data Protection
  - Kubernetes
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/astra-automation/
  - type: API Reference
    url: https://docs.netapp.com/us-en/astra-automation/reference/overview.html
  - type: Getting Started
    url: https://docs.netapp.com/us-en/astra-automation/get-started/overview.html
- name: NetApp StorageGRID API
  description: API for object storage management with StorageGRID.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<storagegrid-endpoint>/api/v3
  humanURL: https://docs.netapp.com/us-en/storagegrid-116/admin/using-grid-management-api.html
  tags:
  - Grid Management
  - Object Storage
  - S3
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/storagegrid-116/admin/using-grid-management-api.html
  - type: S3 API
    url: https://docs.netapp.com/us-en/storagegrid-116/s3/index.html
  - type: Grid Management API (Latest)
    url: https://docs.netapp.com/us-en/storagegrid/admin/using-grid-management-api.html
  - type: S3 REST API Versions and Updates
    url: https://docs.netapp.com/us-en/storagegrid/s3/
  - type: Installation REST APIs
    url: https://docs.netapp.com/us-en/storagegrid-appliances/installconfig/overview-of-installation-rest-apis.html
- name: NetApp Element API
  description: API for NetApp Element software and NetApp HCI storage management.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<mvip>/json-rpc
  humanURL: https://docs.netapp.com/us-en/element-software/api/index.html
  tags:
  - Element
  - HCI
  - JSON-RPC
  - Storage
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/element-software/api/index.html
  - type: API Reference
    url: https://docs.netapp.com/us-en/element-software/api/reference_element_api_reference.html
- name: NetApp Cloud Insights API
  description: API for infrastructure monitoring and analytics.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<tenant>.cloudinsights.netapp.com/rest/v1
  humanURL: https://docs.netapp.com/us-en/cloudinsights/API_Overview.html
  tags:
  - Analytics
  - Monitoring
  - Observability
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/cloudinsights/API_Overview.html
  - type: Authentication
    url: https://docs.netapp.com/us-en/cloudinsights/API_Overview.html#api-access-tokens
- name: NetApp BlueXP Automation API
  description: REST API for automating the administration of cloud-based and on-premises storage resources managed by NetApp BlueXP, including Cloud Volumes ONTAP, on-premises ONTAP, and other BlueXP services.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://cloudmanager.cloud.netapp.com
  humanURL: https://docs.netapp.com/us-en/bluexp-automation/
  tags:
  - BlueXP
  - Cloud Automation
  - Hybrid Cloud
  - Storage Management
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/bluexp-automation/
  - type: API Reference
    url: https://docs.netapp.com/us-en/bluexp-automation/cm/api_reference.html
  - type: Getting Started
    url: https://docs.netapp.com/us-en/bluexp-automation/cm/your_api_call.html
  - type: Platform Concepts
    url: https://docs.netapp.com/us-en/bluexp-automation/platform/concepts.html
  - type: Portal
    url: https://bluexp.netapp.com/
- name: NetApp Active IQ Unified Manager API
  description: REST API for managing and monitoring storage resources on supported NetApp storage systems, including health, performance, capacity, and event management.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<aiqum-host>/api
  humanURL: https://docs.netapp.com/us-en/active-iq-unified-manager/api-automation/concept_get_started_with_um_apis.html
  tags:
  - Active IQ
  - Monitoring
  - Storage Analytics
  - Unified Manager
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/active-iq-unified-manager/api-automation/concept_get_started_with_um_apis.html
  - type: Authentication
    url: https://docs.netapp.com/us-en/active-iq-unified-manager/api-automation/concept_rest_api_access_and_authentication_in_um_apis.html
  - type: Gateway APIs
    url: https://docs.netapp.com/us-en/active-iq-unified-manager/api-automation/concept_gateway_apis.html
  - type: DevNet
    url: https://devnet.netapp.com/aiqum.php
- name: NetApp Active IQ Digital Advisor API
  description: API services for NetApp Active IQ Digital Advisor providing system information, storage efficiency, performance, health, and upgrade insights across your NetApp installed base.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://api.activeiq.netapp.com
  humanURL: https://docs.netapp.com/us-en/active-iq/concept_overview_API_service.html
  tags:
  - Active IQ
  - Digital Advisor
  - Health
  - Monitoring
  - Upgrades
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/active-iq/concept_overview_API_service.html
- name: NetApp SnapCenter API
  description: REST API for automating SnapCenter data protection operations including backup, restore, and clone management for applications and databases.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<snapcenter-host>:8146/api
  humanURL: https://docs.netapp.com/us-en/snapcenter/sc-automation/overview_rest_apis.html
  tags:
  - Backup
  - Clone
  - Data Protection
  - Restore
  - SnapCenter
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/snapcenter/sc-automation/overview_rest_apis.html
  - type: API Reference
    url: https://docs.netapp.com/us-en/snapcenter/sc-automation/reference_supported_rest_apis.html
  - type: Getting Started
    url: https://docs.netapp.com/us-en/snapcenter/sc-automation/task_get_started_with_the_rest_api.html
  - type: Swagger Access
    url: https://docs.netapp.com/us-en/snapcenter/sc-automation/task_how%20to_access_rest_apis_using_the_swagger_api_web_page.html
- name: NetApp E-Series SANtricity Web Services API
  description: RESTful API for managing and monitoring NetApp E-Series and EF-Series storage systems through the SANtricity Web Services Proxy.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<web-services-proxy-host>/devmgr/v2
  humanURL: https://docs.netapp.com/us-en/e-series/web-services-proxy/index.html
  tags:
  - E-Series
  - SANtricity
  - Storage
  - Web Services
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/e-series/web-services-proxy/index.html
  - type: API Reference
    url: https://library.netapp.com/ecmdocs/ECMLP2839901/html/v2.html
  - type: E-Series Documentation
    url: https://docs.netapp.com/us-en/e-series-family/
- name: Azure NetApp Files REST API
  description: REST API for managing Azure NetApp Files resources including NetApp accounts, capacity pools, volumes, and snapshots in Microsoft Azure.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://management.azure.com
  humanURL: https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-develop-with-rest-api
  tags:
  - Azure
  - Cloud Volumes
  - Microsoft Azure
  - Storage
  properties:
  - type: Documentation
    url: https://learn.microsoft.com/en-us/azure/azure-netapp-files/azure-netapp-files-develop-with-rest-api
  - type: API Reference
    url: https://learn.microsoft.com/en-us/rest/api/netapp/
  - type: PowerShell Development Guide
    url: https://learn.microsoft.com/en-us/azure/azure-netapp-files/develop-rest-api-powershell
- name: NetApp ONTAP Tools for VMware vSphere API
  description: REST API for managing ONTAP tools for VMware vSphere, enabling storage provisioning, virtual machine lifecycle management, and vSphere integration.
  image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
  baseURL: https://<ontap-tools-host>:8443
  humanURL: https://docs.netapp.com/us-en/ontap-tools-vmware-vsphere/
  tags:
  - ONTAP
  - Virtualization
  - VMware
  - vSphere
  properties:
  - type: Documentation
    url: https://docs.netapp.com/us-en/ontap-tools-vmware-vsphere/
  - type: API Reference
    url: https://docs.netapp.com/us-en/ontap-tools-vmware-vsphere-104/automation/api-reference.html
  - type: REST API Overview
    url: https://docs.netapp.com/us-en/ontap-tools-vmware-vsphere-102/automation/overview-rest-apis.html
  - type: Getting Started
    url: https://docs.netapp.com/us-en/ontap-tools-vmware-vsphere-10/automation/get-started-with-the-rest-api.html
name: NetApp
tags:
- Cloud
- Data Management
- Hybrid Cloud
- Infrastructure
- Storage
type: Contract
image: https://www.netapp.com/media/na_logo_black_rgb_reg-mark_tcm19-21014.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Collection of NetApp APIs for cloud data services, storage management, and infrastructure.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

