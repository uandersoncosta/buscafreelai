from playwright.async_api import async_playwright
from app.schemas.project import Project

WORKANA_URL = "https://www.workana.com/pt/jobs"

async def search_workana_projects(query: str,) -> list[Project]:
  async with async_playwright() as playwright:
    browser = await playwright.chromium.launch(
      headless=False
    )

    page = await browser.new_page(
      viewport={
        "width": 1440,
        "height": 900,
      }
    )

    search_url = f"{WORKANA_URL}?skills={query}"

    print(f"Pesquisando na Workana: {query}")
    print(f"URL: {search_url}")

    await page.goto(search_url, wait_until="domcontentloaded",)

    await page.wait_for_timeout(5000)

    project_cards = page.locator(".project-item.js-project")

    projects: list[Project] = []

    total_projects = await project_cards.count()

    print(
        f"Projetos encontrados na página: "
        f"{total_projects}"
    )

    for index in range(total_projects):
      card = project_cards.nth(index)

      title_element = card.locator(".project-title a")

      title = (await title_element.inner_text()).strip()

      url = await title_element.evaluate("element => element.href")

      content = (await card.locator(".text-expander-content > span").first.inner_text()).strip()

      bids_text = (await card.locator(".bids").inner_text()).strip()

      budget = (await card.locator(".budget .values > span").inner_text()).strip()

      skills = await card.locator(".skills .skill h3").all_inner_texts()

      skills = [skill.strip() for skill in skills if skill.strip()]

      bids = None

      if bids_text:
          bids = int(
              bids_text
              .replace("Propostas:", "")
              .strip()
          )

      projects.append(
          Project(
              title=title,
              url=url,
              conteudo=content,
              qnt_propostas=bids,
              valor=budget,
              skills=skills,
          )
      )

    await browser.close()

    return projects