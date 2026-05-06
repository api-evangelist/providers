---
aid: skechers-usa
url: https://raw.githubusercontent.com/api-evangelist/skechers-usa/refs/heads/main/apis.yml
name: Skechers U.S.A.
description: Skechers U.S.A. is an American lifestyle and performance footwear company (Fortune 500) that designs, develops, and markets a diverse range of footwear for men, women, and children across 170+ countries. Skechers operates direct-to-consumer digital commerce through its website and mobile app, wholesale partnerships with retailers, and a global network of owned and franchised retail stores. Their digital commerce infrastructure relies on e-commerce APIs for product catalog management, inventory, order management, customer accounts, and loyalty programs.
tags:
  - Footwear
  - Retail
  - E-Commerce
  - Fortune 500
  - Direct-to-Consumer
  - Lifestyle
modified: '2026-05-02'
created: '2026-03-21'
apis:
  - aid: skechers-usa:ecommerce-api
    name: Skechers E-Commerce API
    description: Skechers operates a direct-to-consumer digital commerce platform at skechers.com that enables online shopping for footwear, apparel, and accessories. The platform integrates with e-commerce infrastructure providers for product catalog management, inventory synchronization, order management, shipping, and returns. Third-party integration partners connect via standardized commerce APIs for marketplace listings, affiliate programs, and retailer integrations.
    humanURL: https://www.skechers.com
    baseURL: https://www.skechers.com
    tags:
      - E-Commerce
      - Retail
      - Footwear
      - Product Catalog
    properties:
      - url: https://www.skechers.com
        type: Website
  - aid: skechers-usa:loyalty-api
    name: Skechers Plus Loyalty API
    description: The Skechers Plus loyalty program enables customers to earn and redeem points across all purchase channels (online, in-store, and mobile). The loyalty system integrates with the e-commerce platform, in-store POS systems, and mobile application to provide a unified customer profile and rewards tracking across touchpoints.
    humanURL: https://www.skechers.com/loyalty
    baseURL: https://www.skechers.com
    tags:
      - Loyalty
      - Customer Experience
      - Retail
      - Points
    properties:
      - url: https://www.skechers.com/loyalty
        type: Website
  - aid: skechers-usa:store-locator-api
    name: Skechers Store Locator API
    description: Skechers operates over 4,700 retail stores globally across company-owned, franchise, and licensed formats. The store locator functionality provides geographic search for nearby Skechers retail locations, including store hours, contact information, and available services. This is integrated into the website, mobile app, and third-party mapping services.
    humanURL: https://www.skechers.com/stores
    baseURL: https://www.skechers.com
    tags:
      - Store Locator
      - Retail
      - Geolocation
    properties:
      - url: https://www.skechers.com/stores
        type: Website
common:
  - type: Website
    url: https://www.skechers.com
  - type: Portal
    url: https://www.skechers.com/partners
  - type: JSON-LD
    url: json-ld/skechers-usa-context.jsonld
  - type: Vocabulary
    url: vocabulary/skechers-usa-vocabulary.yml
---
