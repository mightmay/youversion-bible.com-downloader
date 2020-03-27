BOT_NAME = 'bible'

SPIDER_MODULES = ['bible.spiders.spider']
NEWSPIDER_MODULE = 'bible.spiders'

LOG_ENABLED = True

ITEM_PIPELINES = {
    'bible.pipelines.BiblePipeline': 300,
}
