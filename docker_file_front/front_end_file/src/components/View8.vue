<template>
    <div class="title">
        <h3> Scenario 5 - # of Tweets by gcc against income and life </h3>
    </div>
    <div>
        <div ref="chart" style="height: 500px"></div>
        <ul>{{string}}</ul>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            string: '',
            chart: null,
            chartData: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://172.26.135.65:5000/view8');
                console.log(response.data);
                this.chartData = response.data;
                this.updateChart();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart() {
            this.chart.setOption(
                {
                color: ['#5470C6', '#91CC75', '#EE6666'],
                tooltip: {
                    trigger: 'axis',
                    axisPointer: {
                    type: 'cross'
                    }
                },
                grid: {
                    right: '20%'
                },
                toolbox: {
                },
                legend: {
                    data: ['Life', 'Value', '# of Tweets']
                },
                xAxis: [
                    {
                    type: 'category',
                    axisTick: {
                        alignWithLabel: true
                    },
                    // prettier-ignore
                    data: this.chartData[0]
                    }
                ],
                yAxis: [
                    {
                    type: 'value',
                    name: 'life',
                    position: 'right',
                    alignTicks: true,
                    axisLine: {
                        show: true,
                        lineStyle: {
                        color: '#5470C6'
                        }
                    },
                    axisLabel: {
                        formatter: '{value}'
                    }
                    },
                    {
                    type: 'value',
                    name: 'income',
                    position: 'right',
                    alignTicks: true,
                    offset: 80,
                    axisLine: {
                        show: true,
                        lineStyle: {
                        color: '#91CC75'
                        }
                    },
                    axisLabel: {
                        formatter: '{value}'
                    }
                    },
                    {
                    type: 'value',
                    name: '# of Tweets',
                    position: 'left',
                    alignTicks: true,
                    axisLine: {
                        show: true,
                        lineStyle: {
                        color: '#EE6666'
                        }
                    },
                    axisLabel: {
                        formatter: '{value}'
                    }
                    }
                ],
                series: [
                    {
                    name: 'life',
                    type: 'line',
                    data: this.chartData[2]
                    },
                    {
                    name: 'income',
                    type: 'line',
                    yAxisIndex: 1,
                    data: this.chartData[3]
                    },
                    {
                    name: '# of Tweets',
                    type: 'line',
                    yAxisIndex: 2,
                    data: this.chartData[1]
                    }
                ]
                }
            );
        },
    },
    mounted() {
        this.chart = echarts.init(this.$refs.chart);
        this.getData1();
    },
}
</script>

<style lang="scss" scoped>
.title {
    margin-top: 40px;
}
</style>