<p align="center">
    <img width=200 src="https://raw.githubusercontent.com/01walid/it-scoop/master/static/images/logo-colored.png" />
</p>

# it-scoop rebuilt with a static site generator

This migrates [it-scoop.com](https://www.it-scoop.com/) away from Wordpress to [Hugo](https://gohugo.io/) (a static site generator). This makes Youghourta Benali's
content (and all of it-scoop.com co-authors) safer and harder to lose.

# Why
- Portability, this makes it deployable anywhere. No need for a specific hosting. Just a bunch of HTML files to serve straight to the browser.
- Convertible. Markdown files can be [later] converted to PDFs, A book, ..etc. 
- Better performance.
- Little to no maintenance needed.
- Safer with it being on a Git repositor[y|ies]. 
- You can have a local version with just `hugo serve -D` assuming you have [Hugo installed](https://gohugo.io/getting-started/installing/#quick-install).
- Wordpress is a maintainability burden, with ~30 active plugins, it was hard to keep up to date (and safe) without breaking things over the years, even for Youghourta. The site broke recently for more than a week because I updated one plugin, this triggered all this migration process.
- Yes I love to hate Wordpress. It’s unreliable (to me). And this use case doesn’t need its fancy editor. 


# TODO
- [x] Migrate all posts and pages to markdown. Including categories, tags, authors, dates, original URL.
- [x] Download all images. Some posts images use an external URL that is no longer available or is 404. This is an issue even with the existing Wordpress version.
- [x] Each post is browsable and readable on Github itself ([example](/content/posts/2020/2020-02-15-use-youtube-without-youtube-app/index.md)).
- [ ] Fix posts permalinks with arabic text being URL-encoded in markdown. Confusing Hugo and leading to 404 pages.
- [ ] Make the content browsable by category, tag, author.
- [ ] Assign a default thumbnail image to posts without an image (or lost images).
- [ ] Replace it-scoop.com (the current site) with this static version (once I have control over the domain name).
- [ ] Implement Disqus (or equivalent) and import old comments (if I could get access to it-scoop Disqus admin panel).
- [ ] Compare posts one by one. Currently, all posts are automatically processed (with a mix of custom, quickly made, Python and bash scripts).
- [ ] One of the other goals is to kind of modernize the existing Wordpress theme, make a Hugo theme focused on readability. The new theme will use less to no javascript (maybe except for comments).

# Rights and licenses.
- it-scoop [logo and artwork](static/images) is made by [Aissam Hamoud](https://twitter.com/hamoudaissam). You don't have the right to re-use it elsewhere unless you have an explicit permission from Aissam Hamoud.
- it-scoop content itself is licensed under [Creative Commons BY-NC-SA 3.0](https://creativecommons.org/licenses/by-nc-sa/3.0/). This License was chosen by Youghourta himself.
- The theme will be based off [this starter theme](https://github.com/dirkolbrich/hugo-theme-tailwindcss-starter). Licensed under MIT. 

<p align="center">
    <strong>~ لا تنسوا يوغرطة بن علي من صالح دعائكم ~</strong>
</p>
