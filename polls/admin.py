from django.contrib import admin

from .models import Question, Choice


#设计数据内容填写界面
class ChoiceInline(admin.TabularInline):   #增加Choice关联对象，TabularInline列表，StackedInline普通
	model = Choice                       
	extra = 1                              #额外空白Choice


class PollAdmin(admin.ModelAdmin):        #设计Poll数据的fields
	fieldsets = [
	('Question text', {'fields':['question_text']}),  
	('Date information', {'fields':['pub_date']}),
	]
	
	inlines = [ChoiceInline]              #只能用 [] ，()会报错
	
	 #数据显示界面
	list_display = ('question_text', 'pub_date', 'was_published_recently') 

	#pub_date顺序筛选
	list_filter = ['pub_date']

	#搜索功能
	search_fields = ['question_text']     #question_text 为搜索字段

	#change list顶部日期分层导航
	date_hierarchy = 'pub_date'




admin.site.register(Question, PollAdmin)  #注册Question到Admin，排序方式由PollAdmin决定