(function () {
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

  function escapeHtml(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function formatDate(iso) {
    var parts = String(iso).split("-");
    var year = parts[0];
    var month = Number(parts[1]);
    var day = Number(parts[2]);
    return MONTHS[month - 1] + " " + day + ", " + year;
  }

  function postHref(base, slug) {
    return base + encodeURIComponent(slug) + "/";
  }

  function emptyHTML() {
    return '<div class="empty-posts"><p>No posts yet. New ones will show up here.</p></div>';
  }

  function renderList(posts, base) {
    return (
      '<ul class="post-list">' +
      posts
        .map(function (post) {
          return (
            '<li><a href="' +
            postHref(base, post.slug) +
            '"><time datetime="' +
            escapeHtml(post.date) +
            '">' +
            escapeHtml(formatDate(post.date)) +
            "</time>" +
            escapeHtml(post.title) +
            "</a></li>"
          );
        })
        .join("") +
      "</ul>"
    );
  }

  function groupByYear(posts) {
    var groups = [];
    var map = {};
    posts.forEach(function (post) {
      var year = String(post.date).slice(0, 4);
      if (!map[year]) {
        map[year] = [];
        groups.push({ year: year, posts: map[year] });
      }
      map[year].push(post);
    });
    return groups;
  }

  function sortPosts(posts) {
    return posts.slice().sort(function (a, b) {
      if (a.date < b.date) return 1;
      if (a.date > b.date) return -1;
      return 0;
    });
  }

  function renderArchive(posts, base) {
    var groups = groupByYear(posts);
    var html = "";

    if (groups.length > 1) {
      html += '<nav class="year-nav" aria-label="Posts by year">';
      html += groups
        .map(function (group) {
          return '<a href="#year-' + group.year + '">' + group.year + "</a>";
        })
        .join(" · ");
      html += "</nav>";
    }

    groups.forEach(function (group) {
      html += '<section class="year-group" id="year-' + group.year + '">';
      html += "<h3>" + group.year + "</h3>";
      html += renderList(group.posts, base);
      html += "</section>";
    });
    return html;
  }

  function render(root) {
    var src = root.getAttribute("data-posts-src");
    var limit = parseInt(root.getAttribute("data-posts-limit") || "", 10);
    var groupYears = root.getAttribute("data-posts-group") === "year";
    var base = root.getAttribute("data-posts-base") || "";
    var moreHref = root.getAttribute("data-posts-more") || "";
    var heading = root.querySelector("h2");

    fetch(src)
      .then(function (res) {
        return res.json();
      })
      .then(function (posts) {
        if (!Array.isArray(posts) || posts.length === 0) {
          root.innerHTML = (heading ? heading.outerHTML : "") + emptyHTML();
          return;
        }

        var sorted = sortPosts(posts);
        var html = heading ? heading.outerHTML : "";

        if (limit) {
          html += renderList(sorted.slice(0, limit), base);
          if (moreHref && sorted.length > limit) {
            html +=
              '<p class="more-posts"><a href="' +
              escapeHtml(moreHref) +
              '">All posts</a></p>';
          }
        } else if (groupYears) {
          html += renderArchive(sorted, base);
        } else {
          html += renderList(sorted, base);
        }

        root.innerHTML = html;
      })
      .catch(function () {
        /* Keep the static empty state if the index cannot be loaded. */
      });
  }

  document.querySelectorAll("[data-posts-src]").forEach(render);
})();
