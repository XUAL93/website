# Search visibility setup

Technical SEO is included in the local templates. Search-engine verification and submission must be completed after the updated source is deployed to the public site.

## What is included

- Home title and description include Aolong Xu and 徐傲龙.
- Page-specific titles and descriptions, canonical URLs, indexable server-rendered HTML, descriptive image alt text, and responsive image sizes.
- WebSite, Person, and ProfilePage JSON-LD on the homepage, with verified profile URLs.
- Sitemap: https://xual93.github.io/website/sitemap.xml
- Social-sharing metadata and optional Google/Baidu verification meta tags.
- The 404 page has noindex; starter examples are excluded from publishing.

## Publish first

Upload the updated `content`, `config`, `layouts`, `static`, `assets`, `data`, and `scripts` directories, retaining their paths. The original template version does not contain these changes. Wait for the GitHub Pages workflow to succeed.

## Google

1. Open https://search.google.com/search-console/ and add a URL-prefix property for `https://xual93.github.io/website/`.
2. Choose HTML-tag verification. Copy only the verification tag's `content` value into `marketing.verification.google` in `config/_default/params.yaml`.
3. Publish the change, then complete verification in Search Console. Keep the token in the configuration.
4. Submit `sitemap.xml` in Sitemaps for this property.
5. Inspect the homepage URL and request indexing. Monitor Page indexing and URL Inspection for the result.

Use a URL-prefix property for this GitHub Pages project path. A domain property for github.io requires DNS ownership that this project does not provide.

## Baidu

1. Open https://ziyuan.baidu.com/site/index and add/verify the website using a method offered by the account.
2. If HTML-tag verification is available for the submitted address, copy the tag's `content` value into `marketing.verification.baidu`, publish, then verify.
3. Use the platform's ordinary indexing submission and crawl diagnostics. The available submission methods depend on the verified site and account.
4. If verification requires a file or meta tag at the hostname root, this `/website/` project cannot publish to `https://xual93.github.io/`. Root-level verification needs control of the root Pages repository or a domain hosted for this site.

## Baidu and github.io

Baidu crawls github.io poorly and may not index it at all. A custom domain is the reliable route for both engines. Point a domain you own to GitHub Pages (add a CNAME file and set the domain in repository settings), then change `baseURL` in `config/_default/hugo.yaml`. A root domain also fixes the robots.txt and verification problems below.

## Important project-path detail

The generated robots.txt is served at `/website/robots.txt` on the current hosting setup. Crawlers use robots.txt at the hostname root, not a subdirectory. Therefore Search Console sitemap submission is the reliable discovery setup for this project. The robots template will work at the proper root if the site later moves to a root-hosted domain. Check the actual host-root robots rules before diagnosing a crawl problem.

## Discovery and content

Add the website link to the relevant university profile, Google Scholar, ORCID, and LinkedIn where those accounts allow it. Maintain accurate paper titles, author names, and publication status. Keep 徐傲龙 visible as a proper name while the site's prose remains English.

Requesting indexing helps discovery; it does not guarantee immediate inclusion or a ranking position. Google advises that crawling may take days to weeks. Check Search Console instead of relying solely on a `site:` search.

## Official references

- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/crawling-indexing/ask-google-to-recrawl
- https://support.google.com/webmasters/answer/9008080
- https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt
- https://ziyuan.baidu.com/site/index
