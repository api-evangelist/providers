---
aid: google-analytics
url: https://raw.githubusercontent.com/api-evangelist/google-analytics/refs/heads/main/apis.yml
apis:
- aid: google-analytics:google-analytics-data-api-ga4
  name: Google Analytics Data API (GA4)
  description: The Google Analytics Data API provides programmatic access to Google Analytics 4 (GA4) report data.
  image: https://www.google.com/analytics/images/google-analytics-logo.png
  humanURL: https://developers.google.com/analytics/devguides/reporting/data/v1
  baseURL: https://analyticsdata.googleapis.com
  properties:
  - type: Documentation
    url: https://developers.google.com/analytics/devguides/reporting/data/v1
  - type: OpenAPI
    url: https://analyticsdata.googleapis.com/$discovery/rest?version=v1beta
  - type: Authentication
    url: https://developers.google.com/analytics/devguides/reporting/data/v1/quickstart-client-libraries
  - type: Pricing
    url: https://developers.google.com/analytics/devguides/reporting/data/v1/quotas
  tags:
  - Analytics
  - Data API
  - GA4
  - Reporting
- aid: google-analytics:google-analytics-admin-api
  name: Google Analytics Admin API
  description: The Analytics Admin API allows programmatic access to configuration data for Google Analytics 4 properties.
  image: https://www.google.com/analytics/images/google-analytics-logo.png
  humanURL: https://developers.google.com/analytics/devguides/config/admin/v1
  baseURL: https://analyticsadmin.googleapis.com
  properties:
  - type: Documentation
    url: https://developers.google.com/analytics/devguides/config/admin/v1
  - type: OpenAPI
    url: https://analyticsadmin.googleapis.com/$discovery/rest?version=v1beta
  - type: Reference
    url: https://developers.google.com/analytics/devguides/config/admin/v1/rest
  - type: Quickstart
    url: https://developers.google.com/analytics/devguides/config/admin/v1/quickstart-client-libraries
  tags:
  - Admin
  - Configuration
  - GA4
  - Management
- aid: google-analytics:google-analytics-reporting-api-v4
  name: Google Analytics Reporting API v4 (Universal Analytics)
  description: The Analytics Reporting API v4 provides programmatic access to Universal Analytics report data (note Universal Analytics sunset July 1, 2023).
  image: https://www.google.com/analytics/images/google-analytics-logo.png
  humanURL: https://developers.google.com/analytics/devguides/reporting/core/v4
  baseURL: https://analyticsreporting.googleapis.com
  properties:
  - type: Documentation
    url: https://developers.google.com/analytics/devguides/reporting/core/v4
  - type: OpenAPI
    url: https://analyticsreporting.googleapis.com/$discovery/rest?version=v4
  - type: Migration Guide
    url: https://developers.google.com/analytics/devguides/migration/api/reporting-ua-to-ga4
  - type: Deprecation Notice
    url: https://support.google.com/analytics/answer/11583528
  tags:
  - Analytics
  - Deprecated
  - Legacy
  - Reporting
  - Universal Analytics
- aid: google-analytics:google-analytics-management-api-v3
  name: Google Analytics Management API v3
  description: The Analytics Management API allows access to configuration data for Universal Analytics accounts, properties, and views.
  image: https://www.google.com/analytics/images/google-analytics-logo.png
  humanURL: https://developers.google.com/analytics/devguides/config/mgmt/v3
  baseURL: https://www.googleapis.com/analytics/v3
  properties:
  - type: Documentation
    url: https://developers.google.com/analytics/devguides/config/mgmt/v3
  - type: Reference
    url: https://developers.google.com/analytics/devguides/config/mgmt/v3/mgmtReference
  - type: Deprecation Notice
    url: https://support.google.com/analytics/answer/11583528
  tags:
  - Configuration
  - Legacy
  - Management
  - Universal Analytics
name: Google Analytics
tags:
- Analytics
- Data
- Google
- Metrics
- Reporting
- Web Analytics
type: Contract
image: https://www.google.com/analytics/images/google-analytics-logo.png
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: Google Analytics provides data and insights about website and app usage, enabling businesses to understand their audience and optimize their digital properties.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

