import { test, expect } from '@playwright/test';
import { allure, LabelName } from "allure-playwright";
import { LoginPage } from '@lk_pages/login';
import { GenealogicalTreePage } from '@lk_pages/genealogical-tree';

test.describe.configure({ mode: 'parallel', retries: 1});

let page;

test.beforeAll(async ({ browser }) => {
  page = await browser.newPage();
  const loginPage = await new LoginPage(page);
  await loginPage.goto();
  await loginPage.getEmailInput.fill('test@email.ru');
  await loginPage.getPasswordInput.fill('123456');
  await loginPage.toLogin();
});

test.afterEach(async ({}, testInfo) => {
  // Runs after each test and save url on failure.
  if (testInfo.status == 'failed' || testInfo.status == 'passed') {
    const page_url = page.url();
    let page_path = page_url.replace('https://dev-lk.genotek.ru', '');
    page_path = page_path.replace(/\?.*/, '');
    allure.link({ url: page_path, name: "execution_point" });
  }
});

test.afterAll(async () => {
  await page.close();
});

const userIds = [260959];

for (const userId of userIds) {
  test(`Log in as a User_${userId}`, async () => {

    test.info().annotations.push({ 
      type: 'As an', 
      description: 'Client'
    },{ 
      type: 'I want', 
      description: `to be able to log in as a user_${userId} and goto /genealogical-tree page`
    },{ 
      type: 'So that', 
      description: 'I can check the correctness of the data in my personal account'
    });

    const genealogicalTreePage = await test.step(`When User_${userId} goto /genealogical-tree page`, async () => {
      const genealogicalTreePage = await new GenealogicalTreePage(page);
      await genealogicalTreePage.goto();
      return genealogicalTreePage;
    });

    await test.step('Then /genealogical-tree page successfully opened', async () => {
      await expect(genealogicalTreePage.page).toHaveURL(/.*genealogical-tree/);
    });

  });
}
