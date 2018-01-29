$(function(){
    $('.btn-img').on('click', function(){
        $(this).parent().parent().find('.alert').toggle();
    });
    $('#update_form').submit(function (event) {
        event.preventDefault();
        $.ajax({
            method: "POST",
            url: '{% url "models" %}',
            data : {
                'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
            },
            success: function (response) {
                console.log('success');
                onGrowthStageChart();
            }
        })
    });
    $('#select_sam').change(function () {
        onGrowthStageChart();
        onLoadLineChart();
    });
    $('#select_model').change(function () {
        onGrowthStageChart();
    });
    $('#select_season').change(function () {
        onGrowthStageChart();
        onLoadLineChart();
    });

    onLoadLineChart();
    onGrowthStageChart();
});

function onLoadLineChart() {
     var endpoint = '/api/index/data';
     var selected_sam = $('#select_sam').val() + "";
     selected_sam = selected_sam.replace("샘플 번호 ", "");
     var selected_season = $('#select_season').val() + "";
     selected_season = selected_season.replace(" 작기", "");
     $.ajax({
         method: "GET",
         url: endpoint,
         data: {
             'sampleNo':selected_sam,
             'season':selected_season
         },
         success: function (response) {
             var dataList = [];
             dataList.push({
                 label: '# 초장',
                 data: response.leaf_len,
                 lineTension: 0,
                 backgroundColor: 'rgba(255, 99, 132, 0.2)',
                 borderColor: 'rgba(255,99,132,1)',
                 borderWidth: 1
             });
             dataList.push({
                 label: '# 경경',
                 data: response.leaf_n,
                 lineTension: 0,
                 backgroundColor: 'rgba(54, 162, 235, 0.2)',
                 borderColor: 'rgba(54, 162, 235, 1)',
                 borderWidth: 1
             })
             dataList.push({
                 label: '# 화방수',
                 data: response.leaf_width,
                 lineTension: 0,
                 backgroundColor: 'rgba(255, 206, 86, 0.2)',
                 borderColor: 'rgba(54, 162, 235, 1)',
                 borderWidth: 1
             });

             var baseData = {
                 labels: response.labels,
                 datasets: dataList
             };
             var ctx = document.getElementById("lineChart");
             //clear chart
             if (window.line != undefined)
                 window.line.destroy();
             //draw chart
             window.line = new Chart(ctx, {
                 type: 'line',
                 data: baseData,
                 options: {
                     tooltips: {
                         mode: 'x',
                         intersect: false
                     }
                 }
             });
         },
         error: function (error_data) {
             console.log("error");
             console.log(error_data);
         }
     });
 }
function onGrowthStageChart() {
    var endpoint = '/api/growth/data';
    var select_model = $('#select_model').val() + "";
    var selected_sam = $('#select_sam').val() + "";
    selected_sam = selected_sam.replace("샘플 번호 ", "");
    var selected_season = $('#select_season').val() + "";
    selected_season = selected_season.replace(" 작기", "");

    $.ajax({
        method: "GET",
        url: endpoint,
        data: {
            'model':select_model,
            'sampleNo':selected_sam,
            'season':selected_season
        },
        success: function (response) {
            var dataList = [];
            dataList.push({
                label: '# 인식값',
                data: response.predictY,
                lineTension: 0,
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255,99,132,1)',
                borderWidth: 1
            });
            dataList.push({
                label: '# 기준값',
                data: response.predictX,
                lineTension: 0,
                backgroundColor: 'rgba(75, 192, 192, 0.2)',
                borderColor: 'rgba(75, 192, 192, 1)',
                borderWidth: 1
            });
            var baseData = {
                labels: response.predictX,
                datasets: dataList
            };
            var ctx = document.getElementById("growthChart");
            //clear chart
            if (window.growthStageChart != undefined)
                window.growthStageChart.destroy();
            //draw chart
            window.growthStageChart = new Chart(ctx, {
                type: 'line',
                data: baseData,
                options: {
                    showAllTooltips: true,
                    scales: {
                        xAxes: [{
                            ticks: {
                                maxTicksLimit: 25
                            }
                        }]
                    },
                    tooltips: {
                        mode: 'x',
                        intersect: false
                    }
                }
            });
        },
        error: function (error_data) {
            console.log("error");
            console.log(error_data);
        }
    });
}